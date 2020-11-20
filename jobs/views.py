from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import JobTypes,Job,Cities,Resume
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
# Create your views here.
# FBV, CBGV, CBV

# def joblist(request):
#     job_list = Job.objects.order_by('job_type')
#     template = loader.get_template('joblist.html')
#     context = {
#         'job_list':job_list
#     }
#     for job in job_list:
#         job.city_name = Cities[job.job_city][1]
#         job.type_name = JobTypes[job.job_type][1]
#
#     return HttpResponse(template.render(context))

# def jobdetail(request,job_id):
#     job_sing = Job.objects.get(pk = job_id)
#     template = loader.get_template('joblist.html')
#
#     context = {
#
#     }
# def jobdetail(request,job_id):
#     job_single = Job.objects.get(id=job_id)
#     job_single = Job.objects.get(pk=job_id)
#     job_single.city_name = Cities[job_single.job_city][1]
#     context={
#         'job_single':job_single
#     }
#     template = loader.get_template("jobdetail.html")
#
#     # return HttpResponse(template.render({'job_single':job_single}))
#     return render(request,'jobdetail.html',context)
#
#
# class ResumeCreateView(LoginRequiredMixin,CreateView):
#     template_name = 'resume_form.html'
#     success_url = '/'
#     model=Resume
#     fields = [
#         "username","city","phone","email","apply_position","gender",
#         "bachelor_school","master_school","major","degree",
#         "candidate_introduction","work_experience","project_experience"
#     ]
#
#     def get_initial(self):
#         inital={}
#         for x in self.request.GET:
#             inital[x]=self.request.GET[x]
#         return inital
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.applicant = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

def joblist(request):
    job_list = Job.objects.order_by('job_type')
    print(job_list)
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]
    context = {
        'job_list':job_list,
        # "city_name":city_name
    }
    return render(request,'joblist.html',context)
    # return HttpResponse('aaa')

def jobdetail(request, job_id):
    job_single = Job.objects.get(id=job_id)
    job_single.city_name = Cities[job_single.job_city][1]

    return render(request,'jobdetail.html',{'job_single': job_single})
    # return HttpResponse('aaa')


from django.contrib.auth.mixins import LoginRequiredMixin

class ResumeCreateView(LoginRequiredMixin,CreateView):
    template_name = 'resume_form.html'
    success_url = '/'
    model=Resume
    fields = [
        "username","city","phone","email","apply_position","gender",
        "bachelor_school","master_school","major","degree",
        "candidate_introduction","work_experience","project_experience"
    ]

    def get_initial(self):
        inital={}
        for x in self.request.GET:
            inital[x]=self.request.GET[x]
        return inital

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
