from django.urls import path
from jobs.views import joblist,jobdetail
from . import views

urlpatterns = [
    path('', joblist, name="joblist"),
    path('job/<int:job_id>/', jobdetail, name="jobdetail"),
    path('resume/add/', views.ResumeCreateView.as_view(),name='resume-add')
    # path('resume/<int:pk>', views.)
]
