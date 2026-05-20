from django.db import models
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    # True 옵션 시 데이터가 처음 생성될 때 현재 시간 저장
    updated_at = models.DateTimeField(auto_now=True)
    # True 옵션 시 데이터가 저장 될때마다 현재 시간 저장

    def __str__(self): # __str__ 을 함수는 객체(텍스트)를 출력할때 자동으로 호출함
        return f"[{self.pk}]{self.title}"
        # self.pk : 해당 포스트의 pk 값(pk:primary key의 약자)
        # self.title : 해당 포스트의 title 값
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]