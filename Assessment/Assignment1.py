name=input("Enter Student Name: ")
age=int(input("Enter Student Age: "))
degree=input("Enter Student Degree: ")
percentage=float(input("Enter Student Percentage: "))

print("Student Name: ",name)
print("Student Age: ",age)    
print("Student Degree: ",degree)
print("Student Percentage: ",percentage)

#Determine eligibility:Percentage >= 60 → Eligible Percentage < 60 → Not Eligible

if percentage >=60:
    print("Student is Eligible for Admission")
else:
    print("Student is Not Eligible for Admission")

#Calculate: Years remaining to reach age 30 Percentage required to reach 100
years_remaining = 30 - age
percentage_required = 100 - percentage

print("Years remaining to reach age 30: ",years_remaining)
print("Percentage required to reach 100: ",percentage_required)
