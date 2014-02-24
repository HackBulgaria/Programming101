A bunch of simple problems, to warm up with Python. Those are the regular programming problems, that you meet in every beginners course.

The solutions should be written for Python 3.* version.

## Problem 0 - N-th Fibonacci

The most annoying problem of all. Implement a function, called ```nth_fibonacci(n)``` that returns the n-th fibonacci number, given by the argument.

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

## Problem 1 - Sum all digits of a number

Given an integer, implement a function, called ```sum_of_digits(n)``` that calculates the sum of the digits of n.

If a negative number is given, the function should work as if it was positive.

For example, if n is ```1325132435356```, the digit's sum is 43.
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

## Problem 2 - Sum the minimum and maximum elements

Given an array of integers, implement a function, called ```sum_of_min_and_max(arr)```, that calculates and returns the sum of the largest and the smallest integers in the array.

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

## Problem 3 - Sum all divisors of an integer

Given an integer, implement a function, called ```sum_of_divisors(n)``` that calculates the sum of all divisors of n.

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

## Problem 4 - Check if integer is prime

Given an integer, implement a function, called ```is_prime(n)``` which returns True if n is a prime number. You should handle the case with negative numbers too.

A primer number is a number, that is divisible only by 1 and itself.

1 is not considered to be a prime number. [If you are curious why, find out here.](http://www.youtube.com/watch?v=IQofiPqhJ_s)

### Signature

```python
def is_prime(n):
    # implementation
```

### Test examples

```
>>> is_prime(1)
False
>>> is_prime(2)
True
>>> is_prime(8)
False
>>> is_prime(11)
True
>>> is_prime(-10)
False
```

## Problem 5 - Check if a number has a prime number of divisors

Given an integer, implement a function, called ```prime_number_of_divisors(n)``` which returns True if the number of divisors of n is a prime number. False otherwise.

For example, the divisors of 8 are 1,2,4 and 8, a total of 4. 4 is not a prime.
The divisors of 9 are 1,3 and 9, a total of 3, which is a prime number.

### Signature

```python
def prime_number_of_divisors(n):
    # Implementation
```

### Test examples

```
>>> prime_number_of_divisors(7)
True
>>> prime_number_of_divisors(8)
False
>>> prime_number_of_divisors(9)
True
```

## Problem 6 - Are there n sevens in a row?

Implement a function, called ```sevens_in_a_row(arr, n)```, which takes an array of integers ```arr``` and a number ```n > 0```

The function returns True, __if there are n consecutive sevens__ in ```arr```

For example, if ```arr``` is ```[10, 8, 7, 6, 7, 7, 7, 20, -7]``` and n is 3, the function should return True. Otherwise, it returns False

### Signature

```python
def sevens_in_a_row(arr, n)
```

### Test examples

```
>>> sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3)
True
>>> sevens_in_a_row([1,7,1,7,7], 4)
False
>>> sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3)
True
>>> sevens_in_a_row([7,2,1,6,2], 1)
True
```

## Problem 7 - Integer Palindroms

A palindrom is а word or a phrase or a number, that when reversed, stays the same.

For example, the following sequences are palindroms : "azobi4amma4iboza" or "anna".

But this time, we are not interested in words but numbers.
A number palindrom is a number, that taken backwards, remains the same.

For example, the numbers 1, 4224, 9999, 1221 are number palindroms.

Implement a function, called ```is_int_palindrom(n)``` which takes an integer and returns True, if this integer is a palindrom.

### Signature

```python
def is_int_palindrom(n):
    # implementation
```

### Test examples

```
>>> is_int_palindrom(1)
True
>>> is_int_palindrom(42)
False
>>> is_int_palindrom(100001)
True
>>> is_int_palindrom(999)
True
>>> is_int_palindrom(123)
False
```

## Problem 8 - Number containing a single digit?

Implement a function, called ```contains_digit(number, digit)``` which checks if ```digit``` is contained by the given ```number```.

```digit``` and ```number``` are integers.

### Signature

```python
def contains_digit(number, digit):
    # Implementation
```

### Test examples

```
>>> contains_digit(123, 4)
False
>>> contains_digit(42, 2)
True
>>> contains_digit(1000, 0)
True
>>> contains_digit(12346789, 5)
False
```

## Problem 9 - Number containing all digits?

Implement a function, called ```contains_digits(number, digits)``` where ```digits``` is a __list of integers__ and a ```number``` is an integer.

The function should return True if __all__ ```digits``` are contained by ```number```

### Signature

```python
def contains_digits(number, digits):
    # Implementation
```

### Test examples

```
>>> contains_digits(402123, [0, 3, 4])
True
>>> contains_digits(666, [6,4])
False
>>> contains_digits(123456789, [1,2,3,0])
False
>>> contains_digits(456, [])
False
```

## Problem 10 - Is number balanced?

A number is called balanced, if we take the middle of it and the sum of the left and right parts are equal.

For example, the number ```1238033``` is balanced, bacause it has a left part, equal to 123, and right part, equal ot 033.

We have : ```1 + 2 + 3 = 0 + 3 + 3 = 6```

A number with only one digit is always balanced.

Implement a function, called ```is_number_balanced(n)``` which checks if the given number is balanced.

### Signature

```python
def is_number_balanced(n):
    # Implementation
```

### Test examples

```
>>> is_number_balanced(9)
True
>>> is_number_balanced(11)
True
>>> is_number_balanced(13)
False
>>> is_number_balanced(121)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True

```

## Problem 11 - Counting substrings

Implement a function, called ```count_substrings(haystack, needle)``` which returns the count of occurrences of the string ```needle``` in the string ```haystack```.

__Don't count overlapped substings and take case into consideration!__
For overlapping substrings, check the "baba" example below.

### Signature

```python
def count_substrings(haystack, needle):
    # Implementation
```

### Test examples
```
>>> count_substrings("This is a test string", "is")
2
>>> count_substrings("babababa", "baba")
2
>>> count_substrings("Python is an awesome language to program in!", "o")
4
>>> count_substrings("We have nothing in common!", "really?")
0
>>> count_substrings("This is this and that is this", "this")  # "This" != "this"
2
```

## Problem 12 - Vowels in a string

Implement a function, called ```count_vowels(str)``` which returns the count of all vowels in the given string ```str```. __Count uppercase vowels as well!__

The vowels are ```aeiouy```.

### Signature

```python
def count_vowels(str):
    # Implementation
```

### Test examples

```
>>> count_vowels("Python")
2
>>> count_vowels("Theistareykjarbunga") #It's a volcano name!
8
>>> count_vowels("grrrrgh!")
0
>>> count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
22
>>> count_vowels("A nice day to code!")
8
```

## Problem 13 - Consonants in a string

Implement a function, called ```count_consonants(str)``` which returns the count of all consonants in the given string ```str```. __Count uppercase consonants as well!__

The consonants are ```bcdfghjklmnqrstvwxz```.

### Signature

```python
def count_consonants(str):
    # Implementation
```

### Test examples

```
>>> count_consonants("Python")
4
>>> count_consonants("Theistareykjarbunga") #It's a volcano name!
11
>>> count_consonants("grrrrgh!")
7
>>> count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
44
>>> count_consonants("A nice day to code!")
6
```

## Problem 14 - Turn a number into a list of digits

Implement a function, called ```number_to_list(n)``` which takes an integer ```n``` and returns a list, containing the digits of ```n```

### Signature

```python
def number_to_list(n):
    # Implementation
```

### Test Examples

```
>>> number_to_list(123)
[1, 2, 3]
>>> number_to_list(99999)
[9, 9, 9, 9, 9]
>>> number_to_list(123023)
[1, 2, 3, 0, 2, 3]
```

## Problem 15 - Turn a list of digits into a number

Implement a function, called ```list_to_number(digits)``` which takes a list of digits (integers) and returns the number, containing those digits.

### Signature

```python
def list_to_number(digits):
    # Implementation
```

### Test Examples

```
>>> list_to_number([1,2,3])
123
>>> list_to_number([9,9,9,9,9])
99999
>>> list_to_number([1,2,3,0,2,3])
123023
```

## Problem 16 - Biggest difference between two numbers

Implement a function, called ```biggest_difference(arr)```, which takes an array of integers and returns the biggest difference between any two numbers from the array.

For every two elements from the array ```a``` and ```b```, we are looking for the minimum of ```a - b``` or ```b - a```

### Signature

```python
def biggest_difference(arr):
    # Implementation
```

### Test examples

```
>>> biggest_difference([1,2])
-1
>>> biggest_difference([1,2,3,4,5])
-4
>>> biggest_difference([-10, -9, -1])
-9
>>> biggest_difference(range(100))
-99
```

## Problem 17 - Slope style score

Slope style featured as a new snowboarding discipline in the Sochi 2014 Winter Olympics.

To get a medal, you need to get maximum score from the judges.

All judges give you a score - a floating point number between 0 and 100. When all scores are given, the final score is calculated by the following algorithm:

> Remove the largest and the smallest score. From the rest, take the average.

Implement a function, called ```slope_style_score(scores)``` where ```scores``` is a list of floating point numbers.

The function should calculate and return the final score, according to the algoritm above.

The final score should be rounded to two decimal points. This means that if we get a score ```94.66666666666667``` it should be rounded to ```94.66```

### Signature

```python
def slope_style_score(scores):
    # Implementation
```

### Test examples

```
>>> slope_style_score([94, 95, 95, 95, 90])
94.66
>>> slope_style_score([60, 70, 80, 90, 100])
80.0
>>> slope_style_score([96, 95.5, 93, 89, 92])
93.5
```
## Problem 18 - Increasing sequence?

Implement a function, called ```is_increasing(seq)``` where ```seq``` is a list of integers.

The function should return True, if the given sequence is monotonously increasing.

And before you skip this problem, because of the math terminology, let me explain:

> A sequence is monotonously increasing if for every two elements a and b, that are next to each other (a is before b), we have a < b

For example, ```[1,2,3,4,5]``` is monotonously increasing while ```[1,2,3,4,5,1]``` is not.

### Signature

```python
def is_increasing(seq):
    # Implementation
```

### Test examples

```
>>> is_increasing([1,2,3,4,5])
True
>>> is_increasing([1])
True
>>> is_increasing([5,6,-10])
False
>>> is_increasing([1,1,1,1])
False
```

## Problem 19 - Descreasing sequence?

Implement a function, called ```is_decreasing(seq)``` where ```seq``` is a list of integers.

The function should return True, if the given sequence is monotonously decreasing.

And before you skip this problem, because of the math terminology, let me explain:

> A sequence is monotonously decreasing if for every two elements a and b, that are next to each other (a is before b), we have a > b

For example, ```[5,4,3,2,1]``` is monotonously decreasing while ```[1,2,3,4,5,1]``` is not.

### Signature

```python
def is_decreasing(seq):
    # Implementation
```

### Test examples

```
>>> is_decreasing([5,4,3,2,1])
True
>>> is_decreasing([1,2,3])
False
>>> is_decreasing([100, 50, 20])
True
>>> is_decreasing([1,1,1,1])
False
```

## Problem 20 - What is the sign?

This problem is from the Python 2013 course in FMI. [Link to original problem statement.](http://2013.fmi.py-bg.net/tasks/1)

Implement a function, called ```what_is_my_sign(day, month)``` which takes two integer (one for the day and one for the month) and returns the name of the zodiac for the given time period.

Consider the following zodiac table ([Or check wikipedia](http://en.wikipedia.org/wiki/Zodiac#Table_of_dates)) :

* Aries: 21 March – 20 April
* Taurus: 21 April – 21 May
* Gemini: 22 May – 21 June
* Cancer: 22 June – 22 July
* Leo: 23 July – 22 August
* Virgo: 23 August – 23 September
* Libra: 24 September – 23 October
* Scorpio: 24 October – 22 November
* Sagittarius: 23 November – 21 December
* Capricorn: 22 December – 20 January
* Aquarius: 21 January – 19 February
* Pisces: 20 February – 20 March


### Signature

```python
def what_is_my_sign(day, month):
    # Implementation
```

### Test examples

```
>>> what_is_my_sign(5, 8)
"Leo"
>>> what_is_my_sign(29, 1)
"Aquarius"
>>> what_is_my_sign(30, 6)
"Cancer"
>>> what_is_my_sign(31, 5)
"Gemini"
>>> what_is_my_sign(2, 2)
"Aquarius"
>>> what_is_my_sign(8, 5)
"Taurus"
>>> what_is_my_sign(9, 1)
"Capricorn"
```

## Problem 21 - Integer prime factorization

Given an integer ```n```, we can factor it in the following form:

> n = p1^a1 * p2^a2 * ... * pn^an

Where each p is a prime number and each a is an integer and p^a means p to the power of a.

[This is called prime factorization.](http://mathworld.wolfram.com/PrimeFactorization.html)

Lets see few examples

> 10 = 2^1 * 5^1
> 25 = 5^2
> 356 = 2^2 * 89 ^ 1

Implement a function, called ```prime_factorization(n)``` which takes an integer and returns a list of tuples ```(pi, ai)```, which is the result of the factorization.

The list should be sorted in increasing order of the prime numbers.

### Signature

```python
def prime_factorization(n):
    # Implementation
```

### Test examples

```
>>> prime_factorization(10)
[(2, 1), (5, 1)] # This is 2^1 * 5^1
>>> prime_factorization(14)
[(2, 1), (7, 1)]
>>> prime_factorization(356)
[(2, 2), (89, 1)]
>>> prime_factorization(89)
[(89, 1)] # 89 is a prime number
>>> prime_factorization(1000)
[(2, 3), (5, 3)]
```
## Problem 22 - Calculate coins

This problem is from the [Python 2013 course in FMI](http://2013.fmi.py-bg.net/)

Implement a function, called ```calculate_coins(sum)``` where sum is a floating point number.

The function should return a dictionary, that represents a way to get the sum with minimal number of coins.

__The coins that we can use are with values 1,2,100,5,10,50,20.__

Check the examples below.

### Signature

```python
def calculate_coins(sum):
    # Implementation
```

### Test examples

```
>>> calculate_coins(0.53)
{1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0} # We pay with one coin of value 50 and two coins of value 2 and one coin of value 1 - that's the minimal number of coins to get to 0.53
>>> calculate_coins(8.94)
{1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}
```
