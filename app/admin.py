from django.contrib import admin
from .models import myinfo, job, job_desc


class myinfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'contact', 'objective']

    class Meta:
        model = myinfo


admin.site.register(myinfo, myinfoAdmin)


class jobAdmin(admin.ModelAdmin):
    list_display = ['Role', 'join', 'leave', 'cname', 'desc']

    class Meta:
        model = myinfo


admin.site.register(job, jobAdmin)


class job_descAdmin(admin.ModelAdmin):
    list_display = ['desc']

    class Meta:
        model = job_desc


admin.site.register(job_desc,job_descAdmin)
