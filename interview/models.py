from django.db import models
from django.contrib.auth.models import User

# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = (('建议复试', '建议复试'), ('待定', '待定'), ('放弃', '放弃'))

# 复试面试建议
INTERVIEW_RESULT_TYPE = (('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃'))

DEGREE_TYPE = (("本科","本科"),("硕士","硕士"),("博士","博士"))
# HR终面结论
HR_SCORE_TYPE = (('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'))


class Candidate(models.Model):
    # 基础信息
    userid = models.IntegerField(unique=True, blank=True, null=True, verbose_name='应聘者ID')
    username = models.CharField(max_length=135, verbose_name='姓名')
    city = models.CharField(max_length=135, verbose_name='城市')
    phone = models.CharField(max_length=135, verbose_name='手机号码')
    email = models.EmailField(max_length=135, blank=True, verbose_name='邮箱')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name='应聘职位')
    born_address = models.CharField(max_length=135, blank=True, verbose_name='生源地')
    gender = models.CharField(max_length=135, blank=True, verbose_name='性别')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name='候选人信息备注')

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name='本科学校')
    master_school = models.CharField(max_length=135, blank=True, verbose_name='研究生学校')
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name='博士生学校')
    major = models.CharField(max_length=135, blank=True, verbose_name='专业')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name='学历')

    # 综合能力测评成绩，笔试测评成绩
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                                        verbose_name='综合能力测评成绩')
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name='笔试成绩')

    # 第一轮面试记录
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name='初试分',
                                      help_text='1-5分，极优秀: >=4.5，优秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，较差: <3分')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name='学习能力得分')
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                        verbose_name='专业能力得分')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name='优势')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='顾虑和不足')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name='初试结果')
    first_recommend_position = models.CharField(max_length=256, blank=True, verbose_name='推荐部门')
    first_interviewer_user = models.ForeignKey(User, related_name='first_interviewer_user', blank=True, null=True, on_delete=models.CASCADE, verbose_name='面试官')

    first_remark = models.CharField(max_length=135, blank=True, verbose_name='初试备注')

    # 第二轮面试记录
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name='专业复试得分',
                                       help_text='1-5分，极优秀: >=4.5，优秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，较差: <3分')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name='学习能力得分')
    second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                         verbose_name='专业能力得分')
    second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                      verbose_name='追求卓越得分')
    second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                       verbose_name='沟通能力得分')
    second_pressure_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                verbose_name='抗压能力得分')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name='优势')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='顾虑和不足')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name='专业复试结果')
    second_recommend_position = models.CharField(max_length=256, blank=True, verbose_name='建议方向或推荐部门')
    second_interviewer_user = models.ForeignKey(User, related_name='second_interviewer_user', blank=True, null=True, on_delete=models.CASCADE, verbose_name='二面面试官')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name='专业复试备注')

    # HR终面
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR复试综合等级')
    hr_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR责任心')
    hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                                verbose_name='HR坦诚沟通')
    hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR逻辑思维')
    hr_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR发展潜力')
    hr_stability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name='HR稳定性')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name='优势')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name='顾虑和不足')
    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name='HR复试结果')
    hr_interviewer_user = models.ForeignKey(User, related_name='hr_interviewer_user', blank=True, null=True, on_delete=models.CASCADE, verbose_name='HR面试官')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name='HR复试备注')

    creator = models.CharField(max_length=256, blank=True, verbose_name='候选人数据的创建人')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name='最后编辑者')

    class Meta:
        db_table = 'candidate'
        verbose_name = '应聘者'
        verbose_name_plural = '应聘者'
        permissions = [
            ("export","导出候选人列表"),
            ("notify","通知面试官面试")
        ]

    # Python 2 优先使用这个方法，把对象转换成字符串； 如果没有__unicode__()方法，使用 __str__()方法
    def __unicode__(self):
        return self.username

    # Python 3 直接定义 __str__() 方法即可，系统使用这个方法来把对象转换成字符串
    def __str__(self):
        return self.username

