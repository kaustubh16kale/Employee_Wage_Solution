import random as rm
attendance=rm.randint(0,1)
if attendance==1:
    print("employee is Present")
else:
    print("employee is Absent ")

#uc2
rate_per_hour=20
total_hour=8
print("total Payable wage is",attendance*rate_per_hour*total_hour)