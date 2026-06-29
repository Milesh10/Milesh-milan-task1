#Calendar Module
import calendar as c

print(c.calendar(2026))
print(c.month(1997,6))
print(c.monthrange(2028,8))
print(c.isleap(1919))
print(c.weekday(2023,6,4))
print(c.month_name[4])
print(c.day_name[3])
print(c.leapdays(2000,2026))



#Time Module
import time as t

print(t.time())
print(t.ctime())
print(t.gmtime())
print(t.localtime())
print(t.asctime())
print(t.sleep(2))
print(t.strftime("%d-%m-%y"))
print(t.strptime("08 jun 2024","%d %b %Y"))
print(t.mktime(t.localtime()))
print(t.perf_counter())


# Datetime Module
from datetime import datetime, date, time, timedelta

print(datetime.now())                   
print(date.today())                     
print(datetime.now().date())            
print(datetime.now().time())
print(datetime.now().strftime("%d-%m-%y")) 
print(datetime.strptime("05-06-2026", "%d-%m-%Y"))  
print(datetime.now() + timedelta(days=4)) 
print(datetime.now().timestamp())       
print(datetime.now().weekday())        
print(datetime.now().replace(year=2023))   
