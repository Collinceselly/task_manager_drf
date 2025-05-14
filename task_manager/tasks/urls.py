from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.TaskList.as_view()),
    path('<int:pk>/', views.TaskDetails.as_view()),
    path('users/list/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetails.as_view()),
]