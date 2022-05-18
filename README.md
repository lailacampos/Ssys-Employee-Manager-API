# Ssys Coding Challenge

A simple Django REST API

The solution has been deployed to Heroku:

You can find it **[here](https://ssys-employee-manager-laila.herokuapp.com/)**.

___

## The Problem:

SSYS team is growing every month and now we need to have some application to manage
employee's information and reports. As any application written at SSYS, it must have
an API to allow integrations.

### The Solution:

#### Create the "SSYS Employee Manager" app, an API that must have:

- API with employees CRUD:
  - GET: /employees/ (employee list)
  - POST: /employees/ (employee create)
  - UPDATE /employees/ID/ (employee update)
  - DELETE /employees/ID/ (employee delete)
  - GET /employees/ID/ (employee detail)

- API with reports:

  - GET /reports/employees/salary/ (salary report)
  - GET /reports/employees/age/ (age report)

- Persist data in a database

- Use authentication to access


#### Endpoint to employee list:

Request:

    curl -H "Content-Type: application/json" localhost:8000/employees/

Response:

    [
        {
            "id": "1",
            "name": "Anakin Skywalker",
            "email": "skywalker@ssys.com.br",
            "department": "Architecture",
            "salary": "4000.00",
            "birth_date": "01-01-1983"},
        {
            "id": "2",
            "name": "Obi-Wan Kenobi",
            "email": "kenobi@ssys.com.br",
            "department": "Back-End",
            "salary": "3000.00",
            "birth_date": "01-01-1977"},
        {
            "id": "3",
            "name": "Leia Organa",
            "email": "organa@ssys.com.br",
            "department": "DevOps",
            "salary": "5000.00",
            "birth_date": "01-01-1980"
        }
    ]


#### Endpoint to age range report:

Request:

    curl -H 'Content-Type: application/json' localhost:8000/reports/employees/age/

Response:

    {
        "younger": {
            "id": "1",
            "name": "Anakin Skywalker",
            "email": "skywalker@ssys.com.br",
            "department": "Architecture",
            "salary": "4000.00",
            "birth_date": "01-01-1983"},
        "older": {
            "id": "2",
            "name": "Obi-Wan Kenobi",
            "email": "kenobi@ssys.com.br",
            "department": "Back-End",
            "salary": "3000.00",
            "birth_date": "01-01-1977"},
        "average": "40.00"
    }


#### Endpoint to salary range report:

Request:

    curl -H 'Content-Type: application/json' localhost:8000/reports/employees/salary/

Response:

    {
        "lowest ": {
            "id": "2",
            "name": "Obi-Wan Kenobi",
            "email": "kenobi@ssys.com.br",
            "department": "Back-End",
            "salary": "3000.00",
            "birth_date": "01-01-1977"},
        "highest": {
            "id": "3",
            "name": "Leia Organa",
            "email": "organa@ssys.com.br",
            "department": "DevOps",
            "salary": "5000.00",
            "birth_date": "01-01-1980"},
        "average": "4000.00"
    }