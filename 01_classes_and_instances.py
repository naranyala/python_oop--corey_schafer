#print ('Hello World')
class Employee:
   #pass
def __init__(self, first, last, pay):
   self.first=first
   self.last=last
   self.pay=pay
   self.email=first+'.'+last+'@company.com'

#emp_1=Employee()
#emp_2=Employee()
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)

print(emp_1)
print(emp_2)

emp_1.first='Corey'
emp_1.last='Schafer'
emp_1.email='corey.schafer@company.com'
emp_1.pay=50000

emp_2.first='Test'
emp_2.last='User'
emp_2.email='test.user@company.com'
emp_2.pay=60000

print(emp_1.first)
print(emp_1.first+' '+emp_1.last)
print('---')
print(emp_1.email)
print(emp_2.email)