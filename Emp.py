import random as rm
attendance=rm.randint(0,2)
rate_per_hour=20
total_hour=8
part_time_hour=4
if attendance==1:
    print("employee is Present",attendance*rate_per_hour*total_hour)
elif attendance==2:
    print("employee is present and done a part time ",attendance*rate_per_hour*(total_hour+part_time_hour))
else:
    print("employee is absent")

