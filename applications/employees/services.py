from datetime import datetime
from django.db.models import Min, Max, Avg
from .models import Employee


class EmployeeSalaryReport:
    def __init__(self, lowest, highest, average):
        self.lowest = lowest
        self.highest = highest
        self.average = average


class EmployeeAgeReport:
    def __init__(self, youngest, oldest, average):
        self.youngest = youngest
        self.oldest = oldest
        self.average = average


def get_employee_salary_report():
    salary_report_dict = Employee.objects.aggregate(
        min_salary=Min("salary"),
        max_salary=Max("salary"),
        avg_salary=Avg("salary")
    )
    lowest_salary_employee = Employee.objects.filter(
        salary=salary_report_dict.get("min_salary")
    ).first()
    highest_salary_employee = Employee.objects.filter(
        salary=salary_report_dict.get("max_salary")
    ).first()

    return EmployeeSalaryReport(
        lowest=lowest_salary_employee,
        highest=highest_salary_employee,
        average=salary_report_dict.get("avg_salary")
    )


def get_employee_age_report():
    age_report_dict = Employee.objects.aggregate(
        earliest_birth_date=Min("birth_date"),
        oldest_birth_date=Max("birth_date")
    )
    print(age_report_dict)

    youngest_employee = Employee.objects.filter(
        birth_date=age_report_dict.get("oldest_birth_date")
    ).first()
    oldest_employee = Employee.objects.filter(
        birth_date=age_report_dict.get("earliest_birth_date")
    ).first()

    avg_age = calculate_average_age(age_report_dict)

    return EmployeeAgeReport(
        youngest=youngest_employee,
        oldest=oldest_employee,
        average=avg_age
    )


def get_age_years(datetime_obj: datetime):
    age = datetime.now().year - datetime_obj.year
    return age


def calculate_average_age(age_report_dict):
    age_youngest = get_age_years(age_report_dict.get("earliest_birth_date"))
    age_oldest = get_age_years(age_report_dict.get("oldest_birth_date"))
    average = (age_youngest + age_oldest) / 2
    return average
