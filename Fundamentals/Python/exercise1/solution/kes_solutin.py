import datetime
today= datetime.datetime.today()
print(today)
year= today.year
print(f'the year is : {year}')
name_input= input('enter your name: ')
age_input= int(input('enter your age: '))
month_input= int(input('enter the month you were born: '))
day_input= int(input('enter the day of birth: '))
year_input= int(input('enter the year you were born: '))
born= datetime.datetime(year_input, month_input, day_input)

year_diff= (100 - age_input)
print(f"how many years until I turn 100: {year_diff}")

z= (year_diff+year)
print(f'{name_input} be 100 in the year: {z} ')

old= datetime.datetime(z,month_input,day_input)
print(f'i wil be 100 in: {old}')

howlong= (old - today)
print(f': {howlong.days} days')
