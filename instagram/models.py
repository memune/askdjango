from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    message = models.TextField(verbose_name='내용',
        validators=[MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d', verbose_name='사진')
    tag_set = models.ManyToManyField('Tag', blank=True) 
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')


    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse("instagram:post_detail", args={self.pk})
    

    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='instagram_comment_set', limit_choices_to={'is_public': True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

