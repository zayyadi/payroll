from datetime import datetime, date
from decimal import Decimal

month_date = datetime.strftime(datetime.now(), '%B')

class Grade:
    """ 
    This is an Object for calculating Payroll variable,
     and PAYEE according to the new finance act of the Federal Republic of Nigeria
     The variable can be modified for other countries as well.
    """
    def __init__(self, name: str, gross: int):
        self.name = name
        self.gross = gross

# get annual gross
    def get_annual_gross(self) -> Decimal:
        return self.gross * 12

    def get_basic(self) -> int:
        return self.get_annual_gross() * 40/100

    def get_transport(self) -> int:
        return self.get_annual_gross() * 10/ 100 
    def get_housing(self) -> int:
        return self.get_annual_gross() * 10/100 

    def get_bht(self):
        return self.get_basic() + self.get_housing() + self.get_transport()

    def get_pension_employees(self) -> Decimal:
        if self.get_annual_gross() <= 360000:
            return 0
        return self.get_bht() * 8/100
    def get_pension_employer(self) -> Decimal:
        if self.get_annual_gross() <= 360000:
            return 0
        return self.get_bht() * 10/100

    def get_total_pension(self) -> Decimal:
        return (
            self.get_pension_employees() 
            + self.get_pension_employer()
        )
    
    def pension_logic(self):
        if self.get_annual_gross() <= 360000:
            return self.get_total_pension() == 0
        return self.get_pension_employees()
    
    def twenty_percents(self):
        return self.get_annual_gross() * 20/100
    
    def get_gross_income(self):
        return self.get_annual_gross() - self.pension_logic()

    def get_consolidated(self):
        if self.get_gross_income() * 1/100 > 200000:
            return self.get_gross_income() * 1/100
        return 200000

    def get_consolidated_relief(self):
        return self.get_consolidated() + self.twenty_percents()

    def get_taxable_income(self):
        return (
            self.get_annual_gross() 
            - self.get_consolidated_relief() 
            - self.get_pension_employees()
    )
    """  
        ----------------------------------------------------------------------------------------------------------
        THis Part of the code calculate for the Payee of employee according to the New Finance act
        first #300,000 == 7%
        next #300,000 == 11%
        next #500,000 == 15%
        next #500,000 == 19%
        next #1,600,000 == 21%
        above #3,200,000 == 24%
        ----------------------------------------------------------------------------------------------------------
    """
    # calculate for employee who earn #30,000 and below who are not eligible for Income tax deduction
    def first_taxable(self) -> Decimal:
        if self.get_taxable_income() <= 88000:
            return 0

    # calculate for the first #300,000:00 or less of taxable income
    def second_taxable(self) -> Decimal:
        if self.get_taxable_income() < 300000:
            return (self.get_taxable_income()) * 7 / 100
        elif self.get_taxable_income() >= 300000:
            return 300000 * 7 / 100

    # calculate for the second #300,000:00 or less of taxable income
    def third_taxable(self) -> Decimal:
        if (self.get_taxable_income() - 300000) >= 300000:
            return 300000 * 11 / 100
    
        elif (self.get_taxable_income() - 300000) <= 300000:
            return (self.get_taxable_income() - 300000) * 11 / 100

    # calculate for taxable income reminning after the #600,000 deduction, #500,000:00 or less of taxable income
    def fourth_taxable(self) -> Decimal:
        if (self.get_taxable_income() - 600000) >= 500000:
            return 500000 * 15 / 100
    
        elif (self.get_taxable_income() - 600000) <= 500000:
            return (self.get_taxable_income() - 600000) * 15 / 100

    # calculate for taxable income reminning after the #1,100,000 deduction, second #500,000:00 or less of taxable income
    def fifth_taxable(self) -> Decimal:
        if self.get_taxable_income() - 1100000 >= 500000:
            return 500000 * 19 / 100
        elif (self.get_taxable_income() - 1100000) < 500000:
            return (self.get_taxable_income() - 1100000) * 19 / 100

    # calculate for taxable income reminning after the #1,600,000 deduction, #1,600,000:00 or less of taxable income
    def sixth_taxable(self) -> Decimal:
        if self.get_taxable_income() - 1600000 >= 1600000:
            return 1600000 * 21 / 100

        elif (self.get_taxable_income() - 1600000) < 1600000:
            return (self.get_taxable_income() - 1600000) * 21 / 100
        elif (self.get_taxable_income() - 1600000) <= 0:
            return 0
    # calculate for taxable income reminning after the #3,200,000 deduction, #3,200,000:00 or less of taxable income
    def seventh_taxable(self) -> Decimal:
        if self.get_taxable_income() - 3200000 > 3200000:
            return (self.get_taxable_income() - 3200000) * 24 / 100
        elif (self.get_taxable_income() - 3200000) < 3200000:
            return (self.get_taxable_income() - 3200000) * 24 / 100


    def payee_logic(self)  -> Decimal:
        if self.get_taxable_income() <= 88000:
            return self.first_taxable()
        elif self.get_taxable_income() <= 300000:
            return self.second_taxable()
        elif self.get_taxable_income() >= 300000 and self.get_taxable_income() < 600000:
            return self.second_taxable() + self.third_taxable()
        elif (
            self.get_taxable_income() >= 300000
            and self.get_taxable_income() >= 600000
            and self.get_taxable_income() < 1100000
        ):
            return (
                self.second_taxable()
                + self.third_taxable()
                + self.fourth_taxable()
            )
        elif (
            self.get_taxable_income() >= 1100000
            and self.get_taxable_income() < 1600000
        ):
            return (
                self.second_taxable()
                + self.third_taxable()
                + self.fourth_taxable()
                + self.fifth_taxable()
            )
        elif (
            self.get_taxable_income() >= 1600000
            and self.get_taxable_income() < 3200000
            ):
            return (
                self.second_taxable()
                + self.third_taxable()
                + self.fourth_taxable()
                + self.fifth_taxable()
                + self.sixth_taxable()
            )
        elif (
            self.get_taxable_income() >= 3200000
        ):
            return (
                self.second_taxable()
                + self.third_taxable()
                + self.fourth_taxable()
                + self.fifth_taxable()
                + self.sixth_taxable()
                + self.seventh_taxable()
            )

    def get_net_pay_annual(self) -> Decimal:
        return (
            self.get_gross_income()
            - self.payee_logic()
        )

    def get_net_pay_monthly(self) -> Decimal:
        return self.get_net_pay_annual() / 12

    def __str__(self) -> str:
        return f"dear {self.name} your salary for the month of {month_date} is {self.gross} and your net pay is {self.get_net_pay_monthly():,.2f} and your PAYEE for the month is {self.payee_logic() / 12:,.2f}"

emp = Grade("zayyad", 50000)
print(emp.__str__())
# print(emp.get_taxable_income())
# print(emp.get_consolidated_relief());
# print(emp.get_basic())
# print(emp.get_housing())
# print(emp.get_transport())
# print(emp.get_pension_employees())
# print(emp.get_pension_employer())

