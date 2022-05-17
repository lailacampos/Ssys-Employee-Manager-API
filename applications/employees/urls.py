from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.EmployeeUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.EmployeeDeleteAPIView.as_view()),
    path('<int:pk>/', views.EmployeeDetailAPIView.as_view())
]
