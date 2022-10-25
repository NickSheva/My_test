import calendar
def is_leap(year):
	return "YES" if calendar.isleap(year) else 'NO'


year = int(input())
print(is_leap(year))
