excellent = 0
good = 0
improvement = 0
total = 0

for employee in range(1, 6):

    attendance = float(input("Enter Attendance % : "))

    if attendance == -1:
        print("Stopped")
        break

    elif attendance == 0:
        print("Employee", employee, "Record Skipped")
        continue

    elif attendance > 100:
        pass
    elif attendance >= 90:
        print("Employee", employee, ": Excellent")
        excellent += 1
        total += 1

    elif attendance >= 75:
        print("Employee", employee, ": Good")
        good += 1
        total += 1

    else:
        print("Employee", employee, ": Improvement Required")
        improvement += 1
        total += 1

print("\nAttendance Summary")
print("Total Employees Processed :", total)
print("Excellent :", excellent)
print("Good :", good)
print("Improvement Required :", improvement)