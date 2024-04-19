#UC8   taking input according to the company
import random as rm
class Company:
    def __init__(self,RATE_PER_HOUR=0,TOTAL_HOUR=0,PART_TIME_HOUR=0):
        self.RATE_PER_HOUR = RATE_PER_HOUR
        self.TOTAL_HOUR = TOTAL_HOUR
        self.PART_TIME_HOUR = PART_TIME_HOUR
        self.WORKING_DAY_PER_MONTH = 0
        self.TOTAL_WORKING_HOURS = 0
        self.CURRENT_DAY = 1
        self.wages_per_day = {}

    def check_attendance(self):
        attendance=rm.randint(0,2)
        match attendance:
            case 1: 
                print("Employee is present ")
                self.WORKING_DAY_PER_MONTH +=1
                self.TOTAL_WORKING_HOURS +=self.TOTAL_HOUR
                self.wages_per_day[self.CURRENT_DAY]=(self.RATE_PER_HOUR*(self.TOTAL_HOUR))
                self.calculate_wage()
                self.work_hours()
            case 2:
                print("Employee is present and done a partime ")
                self.WORKING_DAY_PER_MONTH+= 1
                self.TOTAL_WORKING_HOURS += (self.PART_TIME_HOUR + self.TOTAL_HOUR)
                self.wages_per_day[self.CURRENT_DAY]=(self.RATE_PER_HOUR*(self.PART_TIME_HOUR))
                self.calculate_wage_partime()
                self.work_hours()
            case _ :
                print("Employee is absent")
                self.wages_per_day[self.CURRENT_DAY]="absent"
        self.CURRENT_DAY+=1


    def calculate_wage(self):
        print("Daily wage payable is : ",self.RATE_PER_HOUR*(self.TOTAL_HOUR))
        # wages_per_day.append(RATE_PER_HOUR*(TOTAL_HOUR))

    def calculate_wage_partime(self):
        print("Daily Payable wage includine part time is",self.RATE_PER_HOUR*(self.PART_TIME_HOUR))
        # wages_per_day.append(RATE_PER_HOUR*(TOTAL_HOUR+PART_TIME_HOUR))


    def total_monthly_wage(self):
        print("The total monthly wage for the employee is",self.TOTAL_WORKING_HOURS*self.RATE_PER_HOUR)

    def work_hours(self):
        print("total work hours completed ", self.TOTAL_WORKING_HOURS)



    # def month(self):
    #     while self.CURRENT_DAY<=20:
    #         self.check_attendance()

    #     self.total_monthly_wage()
    #     print(self.wages_per_day)

    def month(self, days=20, total_hour=8, part_time_hour=4):
        self.TOTAL_HOUR = total_hour
        self.PART_TIME_HOUR = part_time_hour
        while self.CURRENT_DAY <= days:
            self.check_attendance()

        self.total_monthly_wage()
        print(self.wages_per_day)


companyA=Company(100,5,5)
companyA.month()

companyB=Company(10,8,5)
companyB.month()

companyC=Company(10,5,20)
companyC.month()

companyD=Company(4,5,9)
companyD.month()