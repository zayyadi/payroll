# PAYROLL MODULE FOR NIGERIA PAYROLL COMPUTATION :+1: 

This python script contain functions that can be used to compute Payroll variables like Basic, Housing, Transport, Employee Pension, Employer Pension, Consolidated relief an Payee.

## USAGE

The object will be initialized with 2  methods Name of employee and gross Pay.


```
from pay import Grade

name = input("Name: ")
gross = int(input("gross: "))

def employee_pay():
    grade = Grade(name=name, gross=gross)
    net_pay = grade.get_net_pay_monthly()
    return net_pay

```
output:
```
251057.33333333334
```


