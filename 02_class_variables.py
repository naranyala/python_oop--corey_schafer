#print('Hello World')
class Employee:
   #pass
   num_of_emps=0
   raise_amount=1.04

   def __init__(self, first, last, pay):
   #def __init__(self, last, first, pay):
      self.first=first
      self.last=last
      self.pay=pay
      self.email=first+'.'+last+'@company.com'

      Employee.num_of_emps+=1

   def fullname(self):
   #def fullname():
      return '{} {}'.format(self.first, self.last)

   def apply_raise(self):
      #self.pay=int(self.pay*1.04)
      #self.pay=int(self.pay*raise_amount)
      #self.pay=int(self.pay*Employee.raise_amount)
      self.pay=int(self.pay*self.raise_amount)

#emp_1=Employee()
#emp_2=Employee()
print('--1')
print(Employee.num_of_emps)
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)

#print(emp_1.pay)
#emp_1.apply_raise
#emp_1.apply_raise()
#print(emp_1.pay)

print('--2')
print(emp_1.__dict__)
print('--3')
#print(Employee.__dict__)

#Employee.raise_amount=1.05
emp_1.raise_amount=1.05
print(emp_1.__dict__)
print('--4')

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#emp_1.raise_amount
#Employee.raise_amount
print('--5')

print(Employee.num_of_emps)