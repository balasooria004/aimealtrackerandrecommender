# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    path('check-calories/', views.index, name='check_calories'),
    # path('index/', views.index, name='index'),
    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile URLs
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/legacy/', views.profile, name='profile'),  # Legacy support
    
    # Meal logging URLs
    path('log-meal/', views.log_meal, name='log_meal'),
    path('delete-meal/', views.delete_meal, name='delete_meal'),
    path('recommend-meal/', views.recommend_meal, name='recommend_meal'),
path('meal-history/', views.meal_history, name='meal_history'),
    # TDEE and nutrition URLs
    path('split-tdee/', views.split_tdee_view, name='split_tdee'),
]

