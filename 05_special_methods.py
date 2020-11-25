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

   def __repr__(self):
      #pass
      return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

   def __str__(self):
      #pass
      return '{} - {}'.format(self.fullname(), self.email)

   def __add__(self, other):
      return self.pay + other.pay

   def __len__(self):
      return len(self.fullname())

emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','Employee',60000)

#print(emp_1)

#print(1+2)
#print('a'+'b')

#print(repr(emp_1))
#print(str(emp_1))
print("---")
#print(emp_1.__repr__())
#print(emp_1.__str__())

#print(1+2)
print("--2")
#print(int.__add__(1, 2))
#print(str.__add__('a', 'b'))

print(emp_1 + emp_2)

print(len('test'))
print('test'.__len__())
print("--n")
print(len(emp_1))