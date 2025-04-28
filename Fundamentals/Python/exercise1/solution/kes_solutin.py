import datetime
today= datetime.datetime.today()
print(today)
year= today.year
print(f'the year is : {year}')

name_input= input('enter your name: ')
age_input= int(input('enter your age: '))
 
year_diff= (100 - age_input)
print(f"how many years until I turn 100: {year_diff}")

z= (year_diff+year)
print(f'{name_input} be 100 in the year: {z} ')