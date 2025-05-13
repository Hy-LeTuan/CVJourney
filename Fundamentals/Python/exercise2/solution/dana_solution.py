import datetime

categories_list = ["PG", "PG-13", "R"]

while True:
    try:

        day = int(input("Enter your day of birth: "))
        month = int(input("Enter your month of birth: "))
        year = int(input("Enter your year of birth: "))

        birth_date = datetime.date(year, month, day)
        now = datetime.date.today() 

        if year < now.year - 100:
            print("Birth date error. Please try again.\n")
            continue
        if birth_date > now:
            print("Birth date error. Please try again.\n")
            continue
        
        age = now.year - birth_date.year

        if now.month < month:
           age -= 1
        elif now.month == month:
            if now.day < day:
                age -= 1



        print("Movie categories:", categories_list)
        print(age)

        if age >= 17:
            print("You can watch R-rated, PG-13, PG movies")
        elif age >= 13:
            print("You can watch PG-13 and PG movies")
        elif age <= 12:
            print("You can watch PG movies")
                
        break 

    except ValueError:
        print("Invalid input. Please enter valid numbers for day, month, and year.\n")
    

