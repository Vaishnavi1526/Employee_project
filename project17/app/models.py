from django.db import models

class Employee(models.Model):
    Empno=models.IntegerField()
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Mgr=models.IntegerField()
    Hire_Date=models.DateField()
    Sal=models.IntegerField()
    Comm=models.IntegerField()
    Deptno=models.IntegerField(4,primary_key=True)
class Department(models.Model):
    Dept_No=models.IntegerField()
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
class Salgrade(models.Model):
    Grade=models.IntegerField()
    Low_Sal=models.IntegerField()
    Hi_sal=models.IntegerField()
               
    

