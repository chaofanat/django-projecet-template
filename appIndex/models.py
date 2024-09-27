from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class application(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    #描述中可能存在html语言
    description = models.TextField()
    url = models.URLField()
    icon = models.ImageField(upload_to='appIndex/app_icon',default='appIndex/app_icon/default.png')
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("application")
        verbose_name_plural = _("applications")
        ordering = ('-create_time',)