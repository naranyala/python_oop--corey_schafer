#Python OOP
class Employee:
   num_of_emps=0
   #raise_amount=1.04
   raise_amt=1.04

   def __init__(self, first, last, pay):
      self.first=first
      self.last=last
      self.pay=pay
      self.email=first+'.'+last+'@company.com'

      Employee.num_of_emps+=1

   def fullname(self):
      return '{} {}'.format(self.first, self.last)

   def apply_raise(self):
      self.pay=int(self.pay*self.raise_amt)

   @classmethod
   def set_raise_amt(cls, amount):
      #pass
      cls.raise_amt=amount

   @classmethod
   def from_string(cls, emp_str):
      #pass
      first, last, pay = emp_str.split('-')
      return cls(first, last, pay)

   @staticmethod
   def is_workday(day):
      if day.weekday() == 5 or day.weekday() == 6:
         return False
      return True

class Developer(Employee):
#class Developer():
   #pass
   raise_amt=1.10
   def __init__(self, first, last, pay, prog_lang):
      super().__init__(first, last, pay)
      #or
      #Employee.__init__(self, first, last, pay)
      self.prog_lang=prog_lang

class Manager(Employee):
#class Manager():
   def __init__(self, first, last, pay, employees=None):
      super().__init__(first, last, pay)
      if employees is None:
         self.employees = []
      else:
         self.employees = employees

   def add_emp(self, emp):
      if emp not in self.employees:
         self.employees.append(emp)

   def remove_emp(self, emp):
      if emp in self.employees:
         self.employees.remove(emp)

   def print_emps(self):
      for emp in self.employees:
         print('-->', emp.fullname())

#dev_1=Employee('Corey','Schafer',50000)
#dev_2=Employee('Test','User',60000)
dev_1=Developer('Corey','Schafer',50000,"Python")
dev_2=Developer('Test','Employee',60000, "Java")

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print("---")
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print("---")
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
print("---")
#print(mgr_1.email)
#mgr_1.add_emp(dev_2)
#mgr_1.remove_emp(dev_1)
#mgr_1.print_emps()
print("---")
#print(help(Developer))
#print(dev_1.email)
#print(dev_1.prog_lang)
#print(dev_2.email)
#print("---")
#print(dev_1.pay)
#print(dev_2.pay)
#dev_1.apply_raise()
#print(dev_1.pay)
#print(dev_2.pay)
