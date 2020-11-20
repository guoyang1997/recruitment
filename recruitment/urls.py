from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path,include
from django.utils.translation import gettext as _
from jobs import views

from jobs import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('grappelli/', include('grappelli.urls')),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # path('resume/add/', views.ResumeCreateView.as_view(),name='resume-add')
    # url(r'^accounts/profile/',
    #
    #     TemplateView.as_view(template_name='profile.html'),
    #
    #     name='profile'),
]

admin.site.site_header = _("北京网络科技招聘管理系统")