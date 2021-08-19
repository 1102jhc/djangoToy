
from django.db import models
from datetime import datetime

# Create your models here.

class notice_list(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=4000)
    writer = models.CharField(max_length=10)
    write_dttm = models.DateTimeField(default=datetime.now())
    good_cnt = models.IntegerField(default=0)