import datetime

watchable_movies = []
today = datetime.datetime.today()

def check_input(input_type):
    while True: 
        try:
            if input_type == "date":
                user_birth_date = int(input("Type your birth date: "))
                if user_birth_date > 31 or user_birth_date <= 0:
                    raise ValueError ("You entered invalid birthday!")
                return user_birth_date
            
            elif input_type == "month":
                user_birth_month = int(input("Type your birth month: "))
                if user_birth_month > 12 or user_birth_month <= 0:
                    raise ValueError ("You entered invalid month of birth")
                return user_birth_month
            
            elif input_type == "year":
                user_birth_year = int(input("Type your brith year: "))
                if abs(user_birth_year - (today.year)) > 200:
                    raise ValueError ("You entered invalid year of birth")
                return user_birth_year
            
        except ValueError as e:
            print(e)
            
        except:
            print("Enter only valid Answer")

            
def main():
    user_birth_date = check_input("date")
    user_birth_month = check_input("month")
    user_birth_year = check_input("year")

    birthday_obj = datetime.datetime(user_birth_year, user_birth_month, user_birth_date)
            
    current_age = (today - birthday_obj).days / 365
    #there is a problem here with leap years with 365 days 

    if current_age > 17:
        watchable_movies.extend(["R", "PG", "PG-13"])

    elif current_age <= 17 and current_age > 12:
        watchable_movies.extend(["PG", "PG-13"])
    else:
        watchable_movies.append("PG")

    print(f'Age: {current_age}')
    print(f'Watchable Movies: {watchable_movies}')
    return

if __name__ == "__main__":
    main()

