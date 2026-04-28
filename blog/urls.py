from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
    # '' = 내가 찾을 blog의 위치(경로)
    # view.index = views 안의 함수나 클래스를 찾아보겠다
]

# 데이터베이스 안에 키를 딱 하나 찍어서 가져온다 는 것