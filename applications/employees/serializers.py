from datetime import datetime
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'departament', 'salary', 'birth_date']


class EmployeeSalaryReportSerializer(serializers.Serializer):
    lowest = EmployeeSerializer()
    highest = EmployeeSerializer()
    average = serializers.FloatField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class EmployeeAgeReportSerializer(serializers.Serializer):
    youngest = EmployeeSerializer()
    oldest = EmployeeSerializer()
    average = serializers.FloatField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
