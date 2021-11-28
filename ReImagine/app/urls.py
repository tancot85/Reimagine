from django.urls import path

from . import views

urlpatterns = [
    path('', views.content_page, name='homepage'),
    path('content', views.content_page, name='content'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    # path('download_button',views.download_button,name = 'download_button'),

]
