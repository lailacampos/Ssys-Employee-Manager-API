from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReportSalaryListAPIView.as_view()),
]
