from django.db import models

class foodModels(models.Model):
    RATE = (
        ('3','Very good'),
        ('2', 'Good'),
        ('1','Bad'),
    )
    AUTH = (
        ('Admins',(
            ('A','Atid'),
            ('R','Rahmat'),
            ('N','Noora'),
        )),
        ('Normal people',(
            ('Y','Yasin'),
            ('E','Ebne')
        )),

    )
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    desc = models.TextField(default="add descriptions here.")
    rate = models.CharField(max_length=1, choices=RATE)
    auth = models.CharField(max_length=1, choices=AUTH)  # special feature
    img = models.ImageField(upload_to='foodPics/')
    check = models.BooleanField(default=False, verbose_name="آیا اجازه انتشار می‌دهید؟")


    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذاها'

    def __str__(self):
        return self.name
# Create your models here.
