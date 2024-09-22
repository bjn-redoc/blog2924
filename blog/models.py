from django.db import models
from django.utils.html import format_html
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse
from django_resized import ResizedImageField
from django.contrib.auth.models import User


# Create your models here.


# Category model
class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image = ResizedImageField('Header Image',size=[1260,540], upload_to='category/', null=True, blank=True)
    add_date=models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;heigh:40px;border-radius:50%" />'.format(self.image))
    def __str__(self):
        return self.title


# Post Mode
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content = CKEditor5Field('Text', config_name='extends',null=True, blank=True)   
    snippet = CKEditor5Field(max_length=1000, default='Nothing is forever...')
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = ResizedImageField('Header Image',size=[800,500], upload_to='post/', null=True, blank=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    def get_absolute_url(self):
        return reverse('home')
