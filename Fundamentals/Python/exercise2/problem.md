# Exercise 2

**Submission**: To submit the answer to this problem, create a new Git branch with your name.

Then, create a file called `{name}_solution.py` in the `solution/` directory right in this directory. All the code you write should be in the `solution/name_solution.py`.

If I were to submit, I would have a file in the `solution/` directory called `hy_solution.py`.

## Problem

In this problem, you will have to come up with a program that checks if a customer can legally see a specific movie at a cinema or not based on their age and the movie's age restriction.

First, ask the customer for their date of birth, this should include the year, month and date of their birth. Then, decide based on their age what types of movies they are legally allowed to see, which includes 3 categories:

1. If the customer is older than 17, they can watch R-rated movies.
2. If the customer is younger than or equal to 17 and is older than 12, they can see a PG-13 movie.
3. If the customer is younger than or equal to 12, they can only what PG movies.

Your program should print out a list containing the categories that the customer is allowed to watch. For example, if I'm 18, then the program should return

```python
["PG", "PG-13", "R"]
```

## Technical Guide

### Conditionals

A conditional is a way of directing logical flow in a program depending on the current circumstance. Think of it as a conditional in real life, where you would take certain actions based on certain situations, like you should cry at a funeral and laugh at the circus.

A conditional in Python consists of the `if`, `elif` and `else` keywords, which will be followed by a code block with an added level of indentation:

```python
a = 3
b = 2

if a > b:
    print("a is greater than b")
```

In this case, since the condition `a > b` is true, the code block directly following the `if` statement will be executed.

The `elif` keyword (short for else if) can be used to continue the assessment of other conditions, and will only be executed if the `if` statement before it fails.

```python
a = 3
b = 2

# use double equal sign instead of just 1 equal sign in conditionals to check if the 2 variables are equal.
if a == b:
    print("a is greater than b")
elif 3 * a > 2 * b:
    print("3 * a is greater than 2 * b")

# program prints out "a is greater than b"
```

In this example, even though the statement `3 * a > 2 * b` is true, it will not be executed since the first condition is already satisfied. If I split this into 2 `if` statements like this:

```python
a = 3
b = 2

if a > b:
    print("a is greater than b")

if 3 * a > 2 * b:
    print("3 * a is greater than 2 * b")
```

then both `print` statement will be executed.

The `else` keyword is used as a catch all statement where if no conditional statements above it is true, then it will be executed.

```python
a = 1
b = 3

if a > b:
    print("a is greater than b")
elif 3 * a > 2 * b:
    print("3 * a is greater than 2 * b")
else:
    print("none of the above is correct")
```

In this case, since the `if` and `elif` statement are all false, the `else` condition is executed, and the program will print `"none of the above is correct"`.

### List

A **list** in Python is a type of data structure that stores items continuously next to each other.

# Extra

If the problem is too easy for you, you can make it harder by making this program run infinitely until a statement is reached. Try using the

```python
while (condition == true):
    ...
```

loop with error checking so that the customer cannot crash the program. For example, if the user enters a negative age, instead of crashing the program, try catching that mistake with the

```python
try:
    ...
except Error:
    ...
```

statement and run the program until the user enters an age that is resonable.

**Final note:** You can find out more about the `try...except` statement in Python [here](https://www.w3schools.com/python/python_try_except.asp).

That's it for this problem, happy coding and let's suffer together!
