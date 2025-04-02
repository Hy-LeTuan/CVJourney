import datetime

name = input("Name: ")
day = int(input("Birth Date: "))
month = int(input("Birth Month: "))
year = int(input("Birth Year: "))
time = int(input("Birth Time (Hour): "))


today = datetime.datetime.today()
hundard = datetime.datetime(year+100, month, day, time)


remain = hundard - today
timezone = datetime.datetime.now().astimezone().tzinfo
remain_hours = (remain.days * 24)+ remain.seconds//3600


print(f"{name} will turn 100 years old in")
print(f"Years: {hundard.year - today.year} years")
print(f"Days: {remain.days} days")
print(f"Hours: {remain_hours} hours")


