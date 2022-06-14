from pay import Grade


def get_emp_pay(name, gross):
    grade = Grade(name=name, gross=gross)
    annual_gross = grade.get_net_pay_monthly()
    payee = grade.payee_logic()

    return f"Dear {name} your salary for the month is #{annual_gross:,.2f}K and your PAYEE for the month is #{payee / 12:,.2f}K"

print(get_emp_pay("zayyad", 500000))

