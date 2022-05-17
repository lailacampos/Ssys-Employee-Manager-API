from rest_framework import serializers
from applications.employees.models import Employee


class ReportSalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'departament', 'salary', 'birth_date']
