from django.db import models

# https://django-ninja.rest-framework.com/tutorial/other/crud/
# ./manage.py makemigrations
# ./manage.py migrate


class Department(models.Model):
    title = models.CharField(max_length=100)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    birthdate = models.DateField(null=True, blank=True)
