import datetime

def diference(date1,date2):
 
 datediff=date2-date1
 return datediff.days

date1=input("please enter date 1:")
date2=input("pleasea enter date 2:")

try:
    date1=datetime.datetime.strptime(date1,"%Y-%m-%d").date()
    date2=datetime.datetime.strptime(date2,"%Y-%m-%d").date()
    print(diference(date1,date2))
except ValueError:
    print("Please enter date in the format yyyy-mm-dd")
    
