from django.db import models


class myinfo(models.Model):

    email = models.EmailField(max_length=40)
    contact = models.IntegerField()
    objective = models.CharField(max_length=500)
    img = models.ImageField(upload_to='gallery',default="")


class job(models.Model):
    Role = models.CharField(max_length=30)
    join = models.CharField(max_length=15)
    leave = models.CharField(max_length=15)
    cname = models.CharField(max_length=30)
    desc = models.CharField(max_length=500)


class job_desc(models.Model):
    desc = models.CharField(max_length=500)
