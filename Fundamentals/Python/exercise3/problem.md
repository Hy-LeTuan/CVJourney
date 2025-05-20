# Exercise 3

**Submission**: To submit the answer to this problem, create a new Git branch with your name.

Then, create a file called `{name}_solution.py` in the `solution/` directory right in this directory. All the code you write should be in the `solution/name_solution.py`.

If I were to submit, I would have a file in the `solution/` directory called `hy_solution.py`.

## Problem

Create a program that asks the user for a list of numbers, with numbers separated by a space ` ` and then prints out a list of all the divisors of each of the numbers. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

## Technical guide

### The range object

To create a range of number, use the `range` object and its constructor:

```python
x = range(2, 11)
```

Now if you loop over x, you will encounter numbers from $2$ to $11 - 1$:

```python
for elem in x:
print(elem)
```

which when run would print

```python
2
3
4
5
6
7
8
9
10
```

To check if 2 numbers are divisors or not, we need to check for the remainder of their division. If the division is 0, then the divisor is the divisor of the dividend. The **modulo** operation `%` is used to get the remainder of the division:

```python
print(19 % 3)
# 1
```

which prints out $1$ because $19 \div 3 = 6$ and the remainder is $1$.

### Defining a function

A function is a way for us to store and repeat a list of instructions on a variety of different arguments.

To define a function, use the `def` command followed by the function name and its arguments in parenthesis.

```python
def calculate(a, b, c):
    return a + b - 2 * c
```

The variables `a`, `b`, and `c` are arguments to the function, and only exist within the context of the function. This means that these variables are only accessible to the code inside the function, and they change based on the values we pass in when calling the function.

```python
def calculate(a, b, c):
    return a + b - 2 * c

print(a) # Error, a is not defined

print(b) # Error, b is not defined

print(calculate(1, 2, 3)) # 1 + 2 - 2 * 3 = -3

print(calculate(4, 5, 6)) # 4 + 5 - 2 * 6 = -3
```

### The `split` method

The `split` method is a built-in method of any string in Python.

The `split` method does what it says, it splits a single string into a list of strings based on a character or a sequence of character, and the list of split strings does not contain the character the string is split by.

```python

print("hello world", " ".split()" ") # ["hello", "world"]

print("what,is,going,on".split(","))) # ["what", "is", "going", "on"]

print("hellothisisreallycool".split("hello")) # ["", "thisisreallycool"]
```

### The `map` function

The `map` function takes 2 arguments:

1. The first function is a function that takes in any argument.
2. The second function is any `iterable` (could be a list or range) that can be looped over.

The `map` function applies the passed in function to each items in the iterable object and return an iterable that contains return values of the function applied on each list item.

```python
def calculate(a):
    return a + 3 - 2*a


map_result = map(calculate, [1, 2, 3, 4, 5])

for res in map_result:
    print(res)
```

which prints

```
2
1
0
-1
-2
```

and you can reconfirm this answer by applying the calculate function on each item of teh original list.

### Parsing a list of numbers from input

Ask for a list of numbers using the `input` command, then split the string using the `split` function and map the `int` function through using the `map` function. Finally, convert the output to a list using the `list` command.

```python
map_result = list(map(int, input("Enter your list of numbers: ").split(" ")))
```

Run the program and try entering numbers separated by a whitespace, and try to examine the result.

## Extra

To anyone who thinks this is too easy, try combining the last exercise with this one, where you check that all the numbers are valid before finding their divisors.

There are a lot of ways to accomplish this task, but I suggest you define a function to be able to use efficiently.

## Final note

I know this is some very intense theory, but sticking these together and you'll be able to solve this in no time.
