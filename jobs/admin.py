from django.contrib import admin
# Register your models here.
from jobs.models import Job
# admin.site.register(Job)
class JobAdmin(admin.ModelAdmin):
    # 添加
    exclude = ("creator", "created_date", "modified_date")
    list_display = ("job_name", "job_type", "job_city", "creator", "created_date", "modified_date")

    list_filter = ("job_city",)
    search_fields = ('job_name',"job_city","job_type")
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

    # def get_queryset(self, request):

admin.site.register(Job, JobAdmin)
