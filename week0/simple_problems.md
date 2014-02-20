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

For example, if n is 1325132435356, the digit's sum is 43.

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
```
