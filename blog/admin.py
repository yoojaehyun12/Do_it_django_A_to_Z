from django.contrib import admin
from .models import Post # .models 는 현재 폴더의 models.py 에 있는 Post를 사용하자는 뜻
# Register your models here.
# 관리자 페이지에서 아래 코드 추가 시 Post 메뉴가 추가되고 관리 할 수 있음

admin.site.register(Post)
