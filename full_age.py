import datetime

y, m, d = map(int, input().split())
t = datetime.date.today()
b = datetime.date(y, m, d)
how = t - b
print(how.days // 365)

def full_age(y, m, d):
    t = datetime.date.today()
    b = datetime.date(y, m, d)
    how = t.year - b.year - ((t.month,  t.day) < (b.month, b.day))
    return how
print(full_age(1980, 4, 30))

