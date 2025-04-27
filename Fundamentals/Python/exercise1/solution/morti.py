import datetime

name = input("Enter your name: ")

while True:
    try:
        age_str = input("Enter your age: ")
        age = int(age_str)
        if age <= 0:
            print("Please enter a valid age greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number for your age.")

current_year = datetime.datetime.now().year

years_to_100 = 100 - age
year_at_100 = current_year + years_to_100


print(f"Hello {name}! You will turn 100 years old in the year {year_at_100}.")
