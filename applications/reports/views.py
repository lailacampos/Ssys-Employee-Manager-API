from rest_framework import generics
from applications.employees.models import Employee
from applications.employees.serializers import EmployeeSerializer


class ReportSalaryListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        response.data['']

