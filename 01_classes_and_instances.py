#print ('Hello World')
class Employee:
   #pass
   def __init__(self, first, last, pay):
   #def __init__(self, last, first, pay):
      self.first=first
      self.last=last
      self.pay=pay
      self.email=first+'.'+last+'@company.com'

   def fullname(self):
   #def fullname():
      return '{} {}'.format(self.first, self.last)


#emp_1=Employee()
#emp_2=Employee()
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)

#print(emp_1)
#print(emp_2)

#emp_1.first='Corey'
#emp_1.last='Schafer'
#emp_1.email='corey.schafer@company.com'
#emp_1.pay=50000

#emp_2.first='Test'
#emp_2.last='User'
#emp_2.email='test.user@company.com'
#emp_2.pay=60000

print('--1')
print(emp_1.first)
print(emp_1.first+' '+emp_1.last)
print('--2')
print(emp_1.email)
print(emp_2.email)
print('--3')
print('{} {}'.format(emp_1.first, emp_1.last))
print('{} {}'.format(emp_1.first, emp_1.email))
print('--4')
#print(emp_1.fullname)
print(emp_1.fullname())
print(emp_2.fullname())
print('--5')
emp_1.fullname()
print(Employee.fullname(emp_1))
