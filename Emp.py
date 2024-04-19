import random as rm

RATE_PER_HOUR=20
TOTAL_HOUR=8
PART_TIME_HOUR=4
WORKING_DAY_PER_MONTH=20  #assuming employee work for 20 days

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

def total_monthly_wage():
    print("The total monthly wage for the employee is",WORKING_DAY_PER_MONTH*TOTAL_HOUR*RATE_PER_HOUR)

check_attendance()
total_monthly_wage()



