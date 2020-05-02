# Generated by Django 3.0.3 on 2020-03-03 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(limit_choices_to={'is_public': True}, on_delete=django.db.models.deletion.CASCADE, related_name='instagram_comment_set', to='instagram.Post'),
        ),
    ]
