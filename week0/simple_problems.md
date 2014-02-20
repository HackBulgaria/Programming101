A bunch of simple problems, to warm up with Python. Those are the regular programming problems, that you meet in every beginners course.

The solutions should be written for Python 3.* verion.

## Problem 0

The most annoying problem of all. Write a function, called ```nth_fibonacci(n)``` that returns the n-th fibonacci number, given by the argument.

### Signature

```python
def nth_fibonacci(n):
    #implementation here
```

### Test examples

```
>>> nth_fibonacci(1)
1
>>> nth_fibonacci(2)
1
>>> nth_fibonacci(3)
2
>>> nth_fibonacci(10)
55
>>>
```

## Problem 1

Given an integer, write a function, called ```sum_of_digits(n)``` that calculates the sum of the digits of n.

If a negative number is given, the function should work as if it was possitive.

For example, if n is 1325132435356, the digit's sum is 43.
If n is -10, the sum is 1 + 0 = 1

Keep in mind that in Python, there is a special operator for integer division:

```
>>> 5 / 2
2.5
>>> 5 // 2
2
```

### Signature

```python
def sum_of_digits(n):
    # implementation
```

### Test examples

```
>>> sum_of_digits(1325132435356)
43
>>> sum_of_digits(123)
6
>>> sum_of_digits(6)
6
>>> sum_of_digits(-10)
1
```

## Problem 2

Given an array of integers, write a function, called ```sum_of_min_and_max(arr)```, that calculates and returns the sum of the largest and the smallest integers in the array.

Don't bother for the case when the array is empty.

### Signature

```python
def sum_of_min_and_max(arr):
    # implementation
```

### Test examples
```
>>> sum_of_min_and_max([1,2,3,4,5,6,8,9])
10
>>> sum_of_min_and_max([-10,5,10,100])
90
>>> sum_of_min_and_max([1])
2
```

## Problem 3

Given an integer, write a function, called ```sum_of_divisors(n)``` that calculates the sum of all divisors of n.

For example, the divisors of 8 are 1,2,4 and 8 and ```1 + 2 + 4 + 8 = 15```
The divisors of 7 are 1 and 7, which makes the sum = 8

### Signature

```python
def sum_of_divisors(n):
    # implementation
```

### Test examples

```
>>> sum_of_divisors(8)
15
>>> sum_of_divisors(7)
8
>>> sum_of_divisors(1)
1
>>> sum_of_divisors(1000)
2340
```
