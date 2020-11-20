from django.contrib import admin
from django.db.models import Q
from django.utils.safestring import mark_safe

from interview.dingtalk import send
from interview.models import Candidate
import csv
from datetime import datetime
from django.http import HttpResponse
# Register your models here.
from jobs.models import Resume
from django.contrib import messages
exportable_fields = ('username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree', 'first_result', 'first_interviewer_user',
                     'second_result', 'second_interviewer_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user')



def enter_interview_process(modeladmin,request,queryset):
    candidate_names = ''
    for resume in queryset:
        candidate = Candidate()
        #把obj对象中的所有属性拷贝到candidate对象中
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate_names = candidate.username + "," +candidate_names
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request,messages.INFO,'候选人%s已经成功进入面试流程'%(candidate_names))
    send("hello候选人 %s进入面试环节，亲爱的面试官，请准备面试" % (candidate_names))
enter_interview_process.short_description = u"进入面试流程"


def notify_interviewer(modeladmin,request,queryset):
    candidates = ''
    interviewer = ''
    for obj in queryset:
        candidates = obj.username + ";" + candidates
        interviewer = obj.first_interviewer_user.username + ";" + interviewer
    send ("hello候选人 %s进入面试环节，亲爱的面试官，请准备面试：%s"%(candidates,interviewer))
notify_interviewer.short_description=u'通知一面面试官'

def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'recruitment-candidates',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )
    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )

    for obj in queryset:
        ## 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)

    return response

export_model_as_csv.short_description="导出候选人数据到csv"
export_model_as_csv.allowed_permissions=("export",)

# 候选人管理类
export_model_as_csv.short_description = '导出候选人数据到csv'
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')

    actions=(export_model_as_csv,notify_interviewer)
    #当前用户是都有导出权限
    def has_export_permission(self,request):
        opts = self.opts
        return request.user.has_perm('%s,%s '%(opts.app_label,"export"))
    list_display = (
        'username',  'city', 'bachelor_school','get_resume', 'first_score', 'first_result', 'first_interviewer_user', 'second_score',
        'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'hr_interviewer_user','last_editor')
    default_fieldsets = (
        ('基本信息', {'fields': (
            "userid", ("username", "city"), ("phone", "email"), ("apply_position", "born_address"), ("gender", "candidate_remark"),
            ("bachelor_school", "master_school"), ("doctor_school", "major"), ("degree", "test_score_of_general_ability"),
        "paper_score", 'last_editor')}),
        ('第一轮面试记录', {'fields': (
        'first_score', 'first_learning_ability', 'first_professional_competency', 'first_advantage',
        'first_disadvantage', 'first_result', 'first_recommend_position', 'first_interviewer_user', 'first_remark')}),
        ('第二轮专业复试记录', {'fields': (
        'second_score', 'second_learning_ability', 'second_professional_competency', 'second_pursue_of_excellence',
        'second_communication_ability', 'second_pressure_score', 'second_advantage', 'second_disadvantage',
        'second_result', 'second_recommend_position', 'second_interviewer_user', 'second_remark')}),
        ('HR复试记录', {'fields': (
        'hr_score', 'hr_responsibility', 'hr_communication_ability', 'hr_logic_ability', 'hr_potential', 'hr_stability',
        'hr_advantage', 'hr_disadvantage', 'hr_result', 'hr_interviewer_user', 'hr_remark')})
    )
    default_fieldsets_first = (
        (None, {'fields': ("userid", ("username", "city", "phone"),
                           ("email", "apply_position", "born_address", "gender", "candidate_remark"),
                           ("bachelor_school", "master_school", "doctor_school"), ("major", "degree"),
                           "test_score_of_general_ability", "paper_score",)}),
        ('第一轮面试', {'fields': (
            ("first_score", "first_learning_ability", "first_professional_competency"), "first_advantage",
            "first_disadvantage", "first_result", "first_recommend_position", "first_interviewer_user",
            "first_remark",)}),
    )

    default_fieldsets_second = (
        (None, {'fields': ("userid", ("username", "city", "phone"),
                           ("email", "apply_position", "born_address", "gender", "candidate_remark"),
                           ("bachelor_school", "master_school", "doctor_school"), ("major", "degree"),
                           "test_score_of_general_ability", "paper_score",)}),
        ('第一轮面试记录', {'fields': (
            'first_score', 'first_learning_ability', 'first_professional_competency', 'first_advantage',
            'first_disadvantage', 'first_result', 'first_recommend_position', 'first_interviewer_user',
            'first_remark')}),
        ('第二轮面试（专业复试）', {'fields': ("second_score", ("second_learning_ability", "second_professional_competency"), (
            "second_pursue_of_excellence", "second_communication_ability", "second_pressure_score"), "second_advantage",
                                    "second_disadvantage", "second_result", "second_recommend_position",
                                    "second_interviewer_user", "second_remark",)}),
    )

    def get_group_names(self, user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    # 一面面试官仅填写一面反馈， 二面面试官可以填写二面反馈

    def get_fieldsets(self, request, obj=None):
        group_names = self.get_group_names(request.user)
        if 'interviewer' in group_names and obj.second_interviewer_user == request.user and obj.first_interviewer_user ==request.user:
            return self.default_fieldsets_second
        if 'interviewer' in group_names and obj.first_interviewer_user == request.user:
            return self.default_fieldsets_first
        if 'interviewer' in group_names and obj.second_interviewer_user == request.user:
            return self.default_fieldsets_second

        return self.default_fieldsets

    # 对于非管理员，非HR，获取自己是一面面试官或者二面面试官的候选人集合:s
    def get_queryset(self, request):  # show data only owned by the user
        qs = super(CandidateAdmin, self).get_queryset(request)

        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'hr' in group_names:
            return qs
        return Candidate.objects.filter(Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user))

    def get_resume(self, obj):
        if not obj.phone:
            return ""
        resumes = Resume.objects.filter(phone=obj.phone)
        if resumes and len(resumes) > 0:
            return mark_safe(u'<a href="/resume/%s" target="_blank">%s</a' % (resumes[0].id, "查看简历"))
        return ""

    get_resume.short_description = '查看简历'
    get_resume.allow_tags = True

admin.site.register(Candidate, CandidateAdmin)



class ResumeAdmin(admin.ModelAdmin):
    actions = (enter_interview_process,)
    list_display = (
    'username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major', 'created_date')

    readonly_fields = ('applicant', 'created_date', 'modified_date',)

    fieldsets = (
        (None, {'fields': (
            "applicant", ("username", "city", "phone"),
            ("email", "apply_position", "born_address", "gender",),
            ("bachelor_school", "master_school"), ("major", "degree"), ('created_date', 'modified_date'),
            "candidate_introduction", "work_experience", "project_experience",)}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Resume, ResumeAdmin)

