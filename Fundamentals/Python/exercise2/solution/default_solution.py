import datetime

movie_list = ["PG", "PG-13", "R"]

while True:
    try:
        dob = int(input("Date of birth: "))
        mob = int(input("Month of birth: "))
        yob = int(input("Year of birth: "))

        datetime_now = datetime.datetime.now()

        if (dob < 1 or dob > 31):
            raise ValueError("Invalid date of birth")
        elif (mob < 1 or mob > 12):
            raise ValueError("Invalid month of birth")
        elif (abs(yob - datetime_now.year) >= 200):
            raise ValueError("Invalid year of birth")

        age = (datetime_now - datetime.datetime(yob, mob, dob)).days / 365

        movie_category_upto = 3 - (age <= 17) - (age <= 13)

        for i in range(0, movie_category_upto):
            print(f"User is allowed to watch {movie_list[i]} movies")

    except TypeError:
        print("Value entered is not a number")
    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print()
        break
    except:
        print("Error encountered, please try again.")
