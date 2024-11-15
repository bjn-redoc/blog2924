# Generated by Django 4.2.16 on 2024-09-22 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1260, 540], upload_to='category/', verbose_name='Header Image')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Text')),
                ('snippet', django_ckeditor_5.fields.CKEditor5Field(default='Nothing is forever...', max_length=1000)),
                ('url', models.CharField(max_length=100)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[800, 500], upload_to='post/', verbose_name='Header Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]
