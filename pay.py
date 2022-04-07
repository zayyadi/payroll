
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
    def get_annual_gross(self):
        return self.gross * 12

    def get_basic(self) -> int:
        return self.get_annual_gross() * 0.4

    def get_transport(self) -> int:
        return self.get_annual_gross() * 0.1 
    def get_housing(self) -> int:
        return self.get_annual_gross() * 0.1 

    def get_bht(self):
        return self.get_basic() + self.get_housing() + self.get_transport()

    def get_pension_employees(self) -> float:
        if self.get_annual_gross() <= 360000:
            return 0
        return self.get_bht() * 0.08
    def get_pension_employer(self) -> float:
        if self.get_annual_gross() <= 360000:
            return 0
        return self.get_bht() * 0.1

    def get_total_pension(self) -> float:
        return (
            self.get_pension_employees 
            + self.get_pension_employer
        )
    
    def pension_logic(self):
        if self.get_annual_gross() <= 360000:
            return self.get_total_pension() == 0
        return self.get_pension_employees()
    
    def twenty_percents(self):
        return self.get_annual_gross() * 0.2
    
    def get_gross_income(self):
        return self.get_annual_gross() - self.pension_logic()

    def get_consolidated(self):
        if self.get_gross_income() * 0.01 > 200000:
            return self.get_gross_income() * 0.01
        return 200000

    def get_consolidated_relief(self):
        return self.get_consolidated() + self.twenty_percents()

    def get_taxable_income(self):
        return self.get_annual_gross() - self.get_consolidated_relief() - self.get_pension_employees()

    def first_taxable(self):
        if self.get_taxable_income() <= 88000:
            return 0


    def second_taxable(self):
        if self.get_taxable_income() < 300000:
            return (self.get_taxable_income()) * 7 / 100
        elif self.get_taxable_income() >= 300000:
            return 300000 * 7 / 100


    def third_taxable(self):
        if (self.get_taxable_income() - 300000) >= 300000:
            return 300000 * 11 / 100

        elif (self.get_taxable_income() - 300000) <= 300000:
            return (self.get_taxable_income() - 300000) * 11 / 100


    def fourth_taxable(self):
        if (self.get_taxable_income() - 600000) >= 500000:
            return 500000 * 15 / 100

        elif (self.get_taxable_income() - 600000) <= 500000:
            return (self.get_taxable_income() - 600000) * 15 / 100


    def fifth_taxable(self):
        if self.get_taxable_income() - 1100000 >= 500000:
            return 500000 * 19 / 100
        elif (self.get_taxable_income() - 1100000) < 500000:
            return (self.get_taxable_income() - 1100000) * 19 / 100

    def sixth_taxable(self):
        if self.get_taxable_income() - 1600000 >= 1600000:
            return 1600000 * 21 / 100

        elif (self.get_taxable_income() - 1600000) < 1600000:
            return (self.get_taxable_income() - 1600000) * 21 / 100

    def seventh_taxable(self):
        if self.get_taxable_income() - 3200000 > 3200000:
            return 3200000 * 24 / 100
        elif (self.get_taxable_income() - 3200000) < 3200000:
            return (self.get_taxable_income() - 3200000) * 24 / 100


    def payee_logic(self):
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
                self.second_taxable
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
            self.get_taxable_income() > 3200000
        
        ):
            return (
                self.second_taxable()
                + self.third_taxable()
                + self.fourth_taxable()
                + self.fifth_taxable()
                + self.sixth_taxable()
                + self.seventh_taxable()
            )

    def get_net_pay_annual(self) -> float:
        return (
            self.get_gross_income() 
            - self.payee_logic()         
        )

    def get_net_pay_monthly(self) -> float:
        return self.get_net_pay_annual() / 12

emp = Grade("zayyad", 300000)
print(emp.payee_logic())
print(emp.get_net_pay_annual())
print(emp.get_net_pay_monthly())
print(emp.__doc__)