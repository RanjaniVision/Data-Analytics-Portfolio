'''class student:
    def __init__(self, name,Rollno,branch):
        self.name = name
        self.rollno = Rollno
        self.branch = branch
    

student1 = student('Ram','S101','CS')
student2 = student('Rohini','S102','IT')
print(student1.name)'''

'''
class Student:
    def __init__(self,name,rollno,branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch
    def tell_details(self):
        print(f"My Name is {self.name}, Roll No: {self.rollno}, Branch: {self.branch}")
student1 = Student('Ram','S101','CS')
student1.tell_details()'''

#inheritance

class Employee:
    def work(self):
        print("Working")
class Manager(Employee):
    pass

m=Manager()
m.work()

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = 50000
employee1 = Employee('Ram')

print(employee1.__salary)   

#Encapsulation
class Student:
    def __init__(self,marks):
        self.__marks = marks
        
    def get_marks(self):
        return self.__marks

student1 = Student(85)
print(student1.get_marks())