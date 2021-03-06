# Generated by Django 3.0.3 on 2020-03-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d', verbose_name='사진'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
    ]
