We are going to solve problems and add tests to them.
Also, we are going to test the Test-Driven-Development approach, where we add the tests first.

To get you started, lets take a look at the following trivial calculator program:

```python
def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def float_division(a, b):
    return a / b

```

If we want to test the program, we can do one of the following:

1. Fire up the console and start testing the functions
2. Implement an automated unit tests, that will handle the things for us

Of course, the approach in 1) is the simplest. But it does not add up! Everytime, we want to make sure our program is running, we have to __manually__ test everything! And this is a lot of time waste.

Usually, approach 2) is the way to go - implement an automated Unit Test, that checks our program for us.

Here is a simple Unit Test for the ```calculator.py``` program:

```python
import calculator
import unittest


class CalculatorTest(unittest.TestCase):
    """Testing the very simple and trivial calculator module"""
    def test_add(self):
        self.assertEqual(5 + 6, calculator.add(5, 6))

    def test_minus(self):
        self.assertEqual(5 - 6, calculator.minus(5, 6))

    def test_multiply(self):
        self.assertEqual(5 * 5, calculator.multiply(5, 5))

    def test_float_division(self):
        self.assertEqual(5 / 2, calculator.float_division(5, 2))


if __name__ == '__main__':
    unittest.main()

```

If we have the following files:

```
$ ls
calculator.py calculator_tests.py
```

__We can run the test like that:__

```
$ python calculator_tests.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## Problem 0 - Get the things going!

So, to do something very simple, go to ```calculator.py``` and add two more functions:

* ```integer_division(a, b)```
* ```modulo(a, b)```

Add two more tests for the new functions and make sure everything is running!


## Problem 1 - String Utils

Implement a Python module, called ```string_utils.py```, with the following functions:

* ```lines(text)``` - Takes a String argument ```text``` and returns a list of strings, where each element is each line in ```text```
* ```unlines(elements)``` - Takes a list of Strings as argument and returns a String, where each element from ```elements``` is joined with new line
* ```words(text)``` - Takes a String argument ```text``` and returns a list of Strings, where each element is a word from ```text```
* ```unwords(elements)``` - The reverse function of ```words```. Takes a list of strings and returns a single string, where each element is joined by a single whitespace - ```" "```

Create a Unit Test file, called ```string_utils_tests.py``` and write as many test cases as you can think of, for those 4 functions.

## Problem 2 - To tab or to space?

When you have your ```string_utils.py``` tested and running, add the following function:

* ```tabs_to_spaces(str, one_tab_n_spaces=4)``` - which takes a string and replaces all tabs in it, with the amount of ```one_tab_n_spaces``` of spaces.  The default is ```1 tab = 4 spaces```.

Here, a tab in a string is represented by the special ```'\t'``` symbol

```
>>> a = "       string"
>>> a
'\tstring'
```

When you have that tested, implement a Python script, called ```spacify.py```, which takes a filename as the only argument and replaces all tabs in that file with 4 spaces.

Use the ```string_utils.py``` module!

## Problem 3 - Test spacify.py

Now, when you have the program ready, implement a Unit Test, to test if ```spacify.py``` is working correctly.

You may want to ```setUp``` and ```tearDown``` your test to prepare examples.

If you want to run a shell command from python, you can use the following:

```python
from subprocess import call

result = call("python program.py", shell=True)
# result will hold the exit status code. 0 means success
```

## Problem 4 - Count files by extension

Implement a program, called ```ext.py```, which takes one argument - a file extension and prints to the output, the number of files with the given extension, that are located in the current directory (From where we run ```ext.py```)

For example:

```
$ ls
ext.py solution.py tests.py omg.txt program.cpp folder/
$ python ext.py .py
3
$ python ext.py py
0
$ python ext.py .cpp
1
```

__Implement a Unit Test, testing ```ext.py```__

## Problem 5 - Count files by extension, extended

Alter the program ```ext.py``` so it takes two arguments:

* the first - destination folder
* the second - file extension

The program prints the number of files with the given file extension, __located in the destination folder.__

__Alter the tests, so they handle the new case.__

Examples:

```
$ ls
ext.py solution.py tests.py omg.txt program.cpp folder/
$ ls folder/
1.py 2.py 3.py 4.py program2.cpp holy_moly.cpp
$ python ext.py folder/ .py
4
$ ls /home/user/code
default.py solution.py tests.py requirements.txt package.json
$ python ext.py /home/user/code .json
1
```

## Problem 6 - A simple bank account

__Using the TDD technique__, implement a python module, called ```bank.py``` which simulates a bank account.

The module looks like that:

```python
def get_balance():
    pass


def deposit_money(amount):
    pass


def withdraw_money(amount):
    pass
```

__The module should follow these rules:__

* Every bank account starts empty, with a zero balance
* You cannot set or deposit negative amount of money - return False if such attempt is made
* Your balance cannot get under 0 - if you attempt to make such transaction, return False


__Remember the rules of TDD:__

1. Write a test that fails
2. Write code so you can pass the test
3. Refactor your code while running the tests after every refactoring
4. Repeat from 1)


## Problem 7 - A simple timer

__Using the TDD technique__, implement a python module, called ```timer.py``` which simulates a simple timer.

The module looks like that (Check the docstrings, for explanation):

```python
def start_timer(seconds):
    '''
    Initiates the timer for the given seconds
    If you start a started time, this should return False
    '''
    pass


def decrease_time():
    '''
    Decreases the timer by 1 second.
    Returns True, if the decreasing is successful
    If the timer is not started, return False
    If the time is over, return False
    '''
    pass


def is_timer_running():
    '''
    Returns True or False, if the timer is running
    and there are still seconds left (> 0)
    '''
    pass


def stop_timer():
    '''
    Stops a running timer
    If the timer is running, return True
    If the timer is not running, return False
    '''
    pass


def seconds_left():
    '''
    Returns how many seconds are left from the timer
    If the timer is not started or if if it's finished, return 0
    '''
    pass

```

__Remember the rules of TDD:__

1. Write a test that fails
2. Write code so you can pass the test
3. Refactor your code while running the tests after every refactoring
4. Repeat from 1)

## Problem 8 - A tic-tac-toe game

__Using the TDD technique__, implement a python module, called ```tictactoe.py``` which simulates a tic-tac-toe game.

For a reference of the rules, check here - http://en.wikipedia.org/wiki/Tic-tac-toe

__This time, we are not going to give you any specification for the python module.__

Just some requirements:

* The game should be playable by two players (We don't want AI for now)
* Player 1 always starts first
* The two players must always play one after another
* There should be a way, to represent the board as a string and print it
* The game should end, when one of the two players wins

Think about the problem. What kind of functions are you going to need?
Write tests first and see if this can help you!

__Remember the rules of TDD:__

1. Write a test that fails
2. Write code so you can pass the test
3. Refactor your code while running the tests after every refactoring
4. Repeat from 1)

## Problem 9 - CSV to JSON

Implement a python program, called ```csv2json.py``` which takes one argument - a CSV (Comma-separated values) file.

The program should create a new file, with the same name as the given argument, but with ```json``` extension and convert the CSV contents to JSON.

### What is CSV?

CSV, or comma-separated values, is a way to represent a tabular data in a text file.

Lets have the following table:

| Language      | Type          | Website  |
| ------------- |:-------------:| -----:|
| Python        | dynamic | http://python.org/ |
| Ruby      | dynamic      |   https://www.ruby-lang.org/en/ |
| JavaScript (Node) | dynamic      |   http://nodejs.org/ |
| C++ | Static typed | http://www.cplusplus.com/ |
| Java | Static typed | http://www.java.com/en/ |

This table, can be represented as the following CSV file:

```csv
Language,Type,Website
Python,dynamic,http://python.org/
Ruby,dynamic,https://www.ruby-lang.org/en/
JavaScript (Node),dynamic,http://nodejs.org/
C++,Static Typed,http://www.cplusplus.com/
Java,Static Typed,http://www.cplusplus.com/
```

As you can see, the first line of the CSV file represents the fields (headers) of the table.

Every next line is a row from the table, where the data from each cell is separated by a comma.

### What is JSON?

A file format, widely used in JavaScript application (And now, everywhere :D), that was developed by Douglas Crockford.

You can find the specification here - http://json.org/

For the table from above, it can be represented like that in JSON:

```json
[
    {
        "Website": "http://python.org/",
        "Type": "dynamic",
        "Language": "Python"
    },
    {
        "Website": "https://www.ruby-lang.org/en/",
        "Type": "dynamic",
        "Language": "Ruby"
    },
    {
        "Website": "http://nodejs.org/",
        "Type": "dynamic",
        "Language": "JavaScript (Node)"
    },
    {
        "Website": "http://www.cplusplus.com/",
        "Type": "Static Typed",
        "Language": "C++"
    },
    {
        "Website": "http://www.cplusplus.com/",
        "Type": "Static Typed",
        "Language": "Java"
    }
]
```

### Examples

Lets have the following ```langs.csv``` file:

```
Language,Type,Website
Python,dynamic,http://python.org/
Ruby,dynamic,https://www.ruby-lang.org/en/
JavaScript (Node),dynamic,http://nodejs.org/
C++,Static Typed,http://www.cplusplus.com/
Java,Static Typed,http://www.cplusplus.com/

```

When we run our script:

```
$ python csv2json.py lang.csv
```

We get the ```lang.json``` file with the following contents:

```json
[
    {
        "Website": "http://python.org/",
        "Type": "dynamic",
        "Language": "Python"
    },
    {
        "Website": "https://www.ruby-lang.org/en/",
        "Type": "dynamic",
        "Language": "Ruby"
    },
    {
        "Website": "http://nodejs.org/",
        "Type": "dynamic",
        "Language": "JavaScript (Node)"
    },
    {
        "Website": "http://www.cplusplus.com/",
        "Type": "Static Typed",
        "Language": "C++"
    },
    {
        "Website": "http://www.cplusplus.com/",
        "Type": "Static Typed",
        "Language": "Java"
    }
]
```

### Tests

After you are done, how can you test the program? Write tests to cover all cases.
