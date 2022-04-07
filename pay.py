
class Grade:

    def __init__(self, name: str, gross: int):
        self.name = name
        self.gross = gross

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

    def get_pension_employees(self):
        if self.get_annual_gross() <= 360000:
            return 0
        return self.get_bht() * 0.08
    def get_pension_employer(self):
        if self.get_annual_gross() <= 360000:
            return 0
        return self.get_bht() * 0.1
    
    def twenty_percents(self):
        return self.get_annual_gross() * 0.2
    
    def gross_income(self):
        return self.get_annual_gross() - self.get_pension_employees()

    def get_consolidated(self):
        if self.gross_income() * 0.01 > 200000:
            return self.gross_income() * 0.01
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
    
    
    

    



emp = Grade("Zayyad", 500000)
print(emp.second_taxable())
print(emp.third_taxable())
print(emp.fourth_taxable())
print(emp.fifth_taxable())
print(emp.sixth_taxable())
print(emp.seventh_taxable())
print(emp.payee_logic())