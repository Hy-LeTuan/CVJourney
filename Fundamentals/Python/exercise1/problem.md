# Exercise 1

**Submission**: To submit the answer to this problem, create a new Git branch with your name. 

Then, create a file called `{name}_solution.py` in the `solution/` directory right in this directory. All the code you write should be in the `solution/name_solution.py`.

If I were to submit, I would have a file in the `solution/` directory called `hy_solution.py`.

## Problem

Create a program that asks the user to **enter their name and their age**. Print out a message addressed to them that tells them the year that they **will turn 100 years old**.

## Technical Guide

### Reading and input conversion

To read a user input in Python, use the `input(message: str)` function which will return the user's input as a `string`:
```python
# the string Enter your input: will be displayed followed by a space for the user to type
user_input = input("Enter your input: ")
```

To convert variables of a type to another, you can directly typecast it with the `type()` command. For example, I have a variable `x = "4"` which is a string, which I can convert to an integer using the `int()` command:
```python
y = int(x)
print(y, type(y)) # 4, <class 'int'>
```

### Formatted string

Whenever you want to pass a variable into a string, you can use the `formatted string` syntax, where the string is prepended with the `'f'` character and pass variables in with the curly braces like this: `f"string inside {variable}"`
```python
x = 3 + 45 
print(f"the number x is: {x}") # the number x is 48
```

## The datetime object

The `datetime` module is a way for you to manipulate date in a clean format in Python. In the `datetime` module, there is a `datetime` class called `datetime` with which you can get the current date using the `today()` method:
```python
import datetime
today = datetime.datetime.today()
print(today) # 2025-03-30 20:03:57.448345
```
The `datetime` class displays the whole date in this formatted string, but you can access each individual component of the date using the various attributes of the `datetime` class. For example, to get the year, you can use the `year` attribute:
```python
import datetime
today = datetime.datetime.today()
year = today.year
print(f"The year is: {year}") # The year is 2025
```

# Problem Guide

**ONLY READ THIS AFTER YOU HAVE ATTEMPTED THE PROBLEM AT LEAST ONCE**

To solve this problem, you first need to ask for the user's name and age with the `input()` command. To calculate what year the user turns 100, you need to be able to subtract 100 with the user's age, which only happens if both of them are numbers. After subtracting, you'll get the number of years until the user turns 100. Add that number to the current year to get the result.

# Extra

If the problem is too easy for you *(I didn't know you were **that** good)*, you can make it harder by asking the user for their specific birthday using with date, month and year. Then, calculate how many days it will take for them to reach their $100^{th}$ birthday. 

This problem is similar to the original one, the only difference is that you might want to manually create a `datime.datetime` object where the date is the date of the $100^{th}$ birthday. Then, try doing some arithmetics with this `datetime` and the current `datetime` to get a `timedelta` object. Then you can get the answer with an attribute from the `timedelta` object. (assuming the hour of the day does not matter).

**For those who dare:** Try taking the time you were born into consideration in your calculation and calculate exactly how many hours you have left until you reach 100!

**Final note:** To learn more about the `datetime` module, I suggest reading this [official documentation](https://docs.python.org/3/library/datetime.html#datetime.tzinfo.utcoffset), especially about the `datetime` and the `timedelta` class.

That's it for this problem, happy coding and let's suffer together!