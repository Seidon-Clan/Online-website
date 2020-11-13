from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name = 'detail_view'),
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),


]
