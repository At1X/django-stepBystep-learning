from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    vip_date = models.DateField(default=timezone.now)

    def is_special_user(self):
        if self.vip_date > date.today():
            return True
        else:
            return False
    is_special_user.boolean = True #baraye change kardan False be zarbdar to admin panel
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

