from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.


JobTypes = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类"),
    (4, "市场营销类")
]

Cities = [
    (0,"北京"),
    (1,"上海"),
    (2,"深圳"),
    (3,"杭州"),
    (4,"广州")
]


class Job(models.Model):

    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name=_("职位类别"))
    job_name = models.CharField(max_length=250, blank=False, verbose_name=_("职位名称"))
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name=_("工作地点"))
    job_responsibility = models.TextField(max_length=1024, verbose_name=_("职位职责"))
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name=_("职位要求"))
    creator = models.ForeignKey(User, verbose_name=_("创建人"), null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name=_("创建日期"), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_("修改日期"), default=datetime.now)

    class Meta:
        verbose_name=('职位')
        verbose_name_plural=('职位')



class Resume(models.Model):
    DEGREE_TYPE=[
        (0,_('本科')),
        (1,_("硕士")),
        (2,_("博士"))
    ]
    username = models.CharField(max_length=135, verbose_name=_('姓名'))
    applicant = models.ForeignKey(User, verbose_name=_("申请人"), null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135, verbose_name=_('城市'))
    phone = models.CharField(max_length=135, verbose_name=_('手机号码'))
    email = models.EmailField(max_length=135, blank=True, verbose_name=_('邮箱'))
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=_('应聘职位'))
    born_address = models.CharField(max_length=135, blank=True, verbose_name=_('生源地'))
    gender = models.CharField(max_length=135, blank=True, verbose_name=_('性别'))

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=_(('本科学校')))
    master_school = models.CharField(max_length=135, blank=True, verbose_name=_(('研究生学校')))
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=(u'博士生学校'))
    major = models.CharField(max_length=135, blank=True, verbose_name=_(('专业')))
    degree = models.SmallIntegerField(choices=DEGREE_TYPE, blank=True, verbose_name=_(('学历')))
    created_date = models.DateTimeField(verbose_name=_("创建日期"), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_("修改日期"), auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name=_(u'自我介绍'))
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name=_(u'工作经历'))
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name=_(u'项目经历'))

    class Meta:
        verbose_name = _('简历')
        verbose_name_plural = _('简历列表')

    def __str__(self):
        return self.username

