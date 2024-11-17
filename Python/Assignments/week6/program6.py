from datetime import date
import date_utils
import date_utils.calculations

date1 = date(2001, 11, 1)  
date2 = date(2001, 11, 9) 
days = 70

print(date_utils.calculations.days_between(date1, date2))

print(date_utils.calculations.add_days(date1, days))