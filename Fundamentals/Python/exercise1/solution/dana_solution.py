import datetime

name = input("Enter your name: ")
d = int(input("Enter your day of birth: "))
m = int(input("Enter your month of birth: "))
y = int(input("Enter your year of birth: "))

day100 = datetime.datetime(y + 100, m, d)
now = datetime.datetime.now()
left = day100 - now

print(f"Hi {name}, you will turn 100 years old in the year {day100.date()}, in {left.days} days or {round(left.total_seconds()//3600)} hours.")