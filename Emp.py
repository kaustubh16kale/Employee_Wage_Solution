import random as rm

RATE_PER_HOUR=20
TOTAL_HOUR=8
PART_TIME_HOUR=4

def check_attendance():
    attendance=rm.randint(0,2)
    match attendance:
        case 1: 
            print("Employee is present ")
            calculate_wage()
        case 2:
            print("Employee is present and done a partime ")
            calculate_wage_partime()
        case _ :
            print("Employee is absent")

def calculate_wage():
    print("Total wage payable is : ",RATE_PER_HOUR*(TOTAL_HOUR))

def calculate_wage_partime():
    print("Total Payable wage includine part time is",RATE_PER_HOUR*(TOTAL_HOUR+PART_TIME_HOUR))

check_attendance()




