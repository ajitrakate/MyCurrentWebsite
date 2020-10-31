from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile/', views.profile, name='profile'),
    path('post_data/<slug:board_identity>/', views.post_data, name='post_data'),
    path('dashboard/<slug:board_identity>/', views.buttons, name='buttons'),    
    path('dashboard/<slug:board_identity>/<slug:button_identity>/', views.change_status ,name='change_status')

]