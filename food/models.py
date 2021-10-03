from django.db import models
from django.utils import timezone
from django.utils.html import format_html

class manageFood(models.Manager):
    def show(self):
        return self.filter(check=True)
class Category(models.Model):
    parent = models.ForeignKey('self', null=True, default=None, blank=True, on_delete=models.SET_NULL, related_name='children')
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'گروه'
        verbose_name_plural = 'گروه‌ ها'

    def __str__(self):
        return self.name

class foodModels(models.Model):
    RATE = (
        ('3','Very good'),
        ('2', 'Good'),
        ('1','Bad'),
    )
    AUTH = (
        ('Admins',(
            ('Atid','Atid'),
            ('Rahmat','Rahmat'),
            ('Noora','Noora'),
        )),
        ('Normal people',(
            ('Yasin','Yasin'),
            ('Ebne','Ebne')
        )),

    )
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    desc = models.TextField(default="add descriptions here.")
    rate = models.CharField(max_length=1, choices=RATE)
    auth = models.CharField(max_length=20, choices=AUTH)  # special feature
    date = models.DateTimeField(default=timezone.now)
    categ = models.ManyToManyField(Category, related_name='categs')
    img = models.ImageField(upload_to='foodPics/')
    check = models.BooleanField(default=False, verbose_name="آیا اجازه انتشار می‌دهید؟")


    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذاها'

    def __str__(self):
        return self.name

    def showPic(self):
        return format_html("<img width=80 height=50 style= 'border-radius:10px;' src='{}'>".format(self.img.url))
    showPic.short_description = 'عکس'
    objects = manageFood()
# Create your models here.
