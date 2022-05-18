from django.urls import path
from applications.reports.views import ReportSalaryAPIView, ReportAgeAPIView

urlpatterns = [
    path('employees/salary/', ReportSalaryAPIView.as_view(), name='report-salary'),
    path('employees/age/', ReportAgeAPIView.as_view(), name='report-age')
]
