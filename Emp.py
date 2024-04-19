import random as rm
#UC9_storing_dailywage_days
RATE_PER_HOUR=20
TOTAL_HOUR=8
PART_TIME_HOUR=4
WORKING_DAY_PER_MONTH=0
TOTAL_WORKING_HOURS=0
CURRENT_DAY=1
wages_per_day={}

def check_attendance():
    global WORKING_DAY_PER_MONTH
    global TOTAL_WORKING_HOURS
    global CURRENT_DAY
    attendance=rm.randint(0,2)
    match attendance:
        case 1: 
            print("Employee is present ")
            WORKING_DAY_PER_MONTH +=1
            TOTAL_WORKING_HOURS +=TOTAL_HOUR
            wages_per_day[CURRENT_DAY]=(RATE_PER_HOUR*(TOTAL_HOUR))
            calculate_wage()
            work_hours()
        case 2:
            print("Employee is present and done a partime ")
            WORKING_DAY_PER_MONTH+= 1
            TOTAL_WORKING_HOURS += (PART_TIME_HOUR + TOTAL_HOUR)
            wages_per_day[CURRENT_DAY]=(RATE_PER_HOUR*(TOTAL_HOUR+PART_TIME_HOUR))
            calculate_wage_partime()
            work_hours()
        case _ :
            print("Employee is absent")
            wages_per_day[CURRENT_DAY]="absent"
    CURRENT_DAY+=1


def calculate_wage():
    print("Total wage payable is : ",RATE_PER_HOUR*(TOTAL_HOUR))
    # wages_per_day.append(RATE_PER_HOUR*(TOTAL_HOUR))

def calculate_wage_partime():
    print("Total Payable wage includine part time is",RATE_PER_HOUR*(TOTAL_HOUR+PART_TIME_HOUR))
    # wages_per_day.append(RATE_PER_HOUR*(TOTAL_HOUR+PART_TIME_HOUR))


def total_monthly_wage():
    print("The total monthly wage for the employee is",TOTAL_WORKING_HOURS*RATE_PER_HOUR)

def work_hours():
    print("total work hours completed ", TOTAL_WORKING_HOURS)




while WORKING_DAY_PER_MONTH <=20 and TOTAL_WORKING_HOURS <=100:
    check_attendance()

total_monthly_wage()
print(wages_per_day)


