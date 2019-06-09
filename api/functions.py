from datetime import datetime

def string_to_date(date):
	day = date[0:2]
	month = date[3:5]
	year = date[6:10]
	return datetime(int(year),int(month),int(day))
	
today = "01-01-2019"
tomorrow = "01-01-2020"
days = string_to_date(tomorrow) - string_to_date(today)
str_days =  str(days)
k = str_days.split(' ')
print(k[0])