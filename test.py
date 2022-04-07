from pay import Grade


emp_name = input('Enter your Name: ')
emp_gross = int(input("Enter Employee gross: "))

def get_emp_pay():
    grade = Grade(name=emp_name, gross=emp_gross)
    annual_gross = grade.get_annual_gross()
    payee = grade.payee_logic()

    return f"{annual_gross} and {payee}"

print(get_emp_pay())