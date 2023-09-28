from django.urls import path
from .views import register, log_in, log_out, UserDetailView

app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('user-info/<int:pk>/', UserDetailView.as_view(), name='user-info'),
]