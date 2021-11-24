from django.urls import path

from . import views

urlpatterns = [
    path('', views.content_page, name='homepage'),
    path('content',views.content_page,name = 'content')
]