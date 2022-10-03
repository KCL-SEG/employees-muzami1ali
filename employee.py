"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class SalaryContractEmployee(Employee):
    def __init__(self, name, salary, bonus=0, contract=0, rate=0):
        super().__init__(name)
        self.salary=salary
        self.bonus=bonus
        self.contract=contract
        self.rate= rate
        self.total=0

    def get_pay(self):
        super().get_pay
        self.total = self.salary
        if self.bonus>0:
            self.total+=self.bonus  
        if self.contract>0:
            self.total += (self.contract * self.rate)
        return self.total

    def __str__(self):
        super().__str__
        if self.bonus==0 and self.contract==0:
            return(f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.salary}.")
        elif self.bonus!=0 and self.contract==0:
            return(f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}.  Their total pay is {self.total}.")
        elif self.bonus==0 and self.contract!=0:
            return(f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contract} contract(s) at {self.rate}/contract.  Their total pay is {self.total}.")

class HourlyContractEmployee(Employee):
    def __init__(self, name, contract,hour, bonus=0, commissioncontract=0, rate=0):
        super().__init__(name)
        self.contract=contract
        self.hour=hour
        self.bonus=bonus
        self.commissioncontract=commissioncontract
        self.rate=rate
        self.total=(self.contract*self.hour)

    def get_pay(self):
        super().get_pay()
        if self.bonus>0:
            self.total+=self.bonus
        elif self.commissioncontract>0:
            self.total += (self.commissioncontract * self.rate)
        return self.total

    def __str__(self):
        super().__str__()
        if self.bonus==0 and self.commissioncontract==0:
            return(f"{self.name} works on a contract of {self.contract} hours at {self.hour}/hour.  Their total pay is {self.total}.")
        elif self.bonus!=0 and self.commissioncontract==0:
            return(f"{self.name} works on a contract of {self.contract} hours at {self.hour}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.total}.")
        elif self.bonus==0 and self.commissioncontract!=0:
            return(f"{self.name} works on a contract of {self.contract} hours at {self.hour}/hour and receives a commission for {self.commissioncontract} contract(s) at {self.rate}/contract.  Their total pay is {self.total}.")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryContractEmployee('Billie', 4000)
# billie.__str__()

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyContractEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContractEmployee('Renee', 3000, contract=4, rate=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContractEmployee('Jan', 150, 25,commissioncontract=3, rate=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryContractEmployee('Robbie', 2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyContractEmployee('Ariel', 120, 30, 600)
