from rest_framework import views
from rest_framework.response import Response

from applications.employees.services import get_employee_salary_report, get_employee_age_report
from applications.employees.serializers import EmployeeSalaryReportSerializer, EmployeeAgeReportSerializer


class ReportSalaryAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        employee_salary_report = get_employee_salary_report()
        serializer = EmployeeSalaryReportSerializer(employee_salary_report)
        return Response(serializer.data)


class ReportAgeAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        employee_age_report = get_employee_age_report()
        serializer = EmployeeAgeReportSerializer(employee_age_report)
        return Response(serializer.data)

