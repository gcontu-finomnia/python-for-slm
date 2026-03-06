# Python Basics Exercises and Solutions

## Exercise 1: Hello World
### Problem:
Write a Python program that prints 'Hello, World!'.

### Solution:
```python
print('Hello, World!')
```

## Exercise 2: Simple Addition
### Problem:
Write a Python program that takes two numbers as input and outputs their sum.

### Solution:
```python
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

sum = num1 + num2
print(f'The sum is: {sum}')
```

## Exercise 3: List Comprehension
### Problem:
Create a list of squares for the numbers from 1 to 10.

### Solution:
```python
squares = [x**2 for x in range(1, 11)]
print(squares)
```

## Exercise 4: Factorial of a Number
### Problem:
Write a Python program to calculate the factorial of a number.

### Solution:
```python
import math

num = int(input('Enter a number: '))
factorial = math.factorial(num)
print(f'The factorial of {num} is {factorial}.')
```
