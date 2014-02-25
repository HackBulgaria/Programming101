# How to run your Python programs and test them.

To illustrate things, let's imagine that we have to imlement a python program, that calculates the sum of two integers.

Here we have the code:

```python
def awesome_sum(a, b):
    return a + b
```

And now, we want to test our function.

We propose two different approaches for this:

## Via console

### Simple import

If your source file is named ```solution.py```, do the following:

* Navigate to the directory, where ```solution.py``` is located;
* Run the python interpreter by typing ```py``` or ```python``` (Depends on the version you have. We need 3.3)
* import the function - ```from solution import awesome_sum``` - The algorithm here is ```from file_name_without_py import function_name```
* Now you have run your funciton :

```
>>> awesome_sum(1,2)
3
```

### main() method

Add main method and a call to it in your ```solution.py``` file:

```python
def awesome_sum(a, b):
    return a + b

def main():
    print(awesome_sum(1,3))
    # more test cases to follow

# This piece of code will call the main method,
# When you run solution.py via the interpreter
if __name__ == '__main__':
    main()
```

After this, you can just call the program with ```py```:

```
$ py solution.py
4
```

## Unit Tests

You can create a file, called ```awesome_sum_tests.py``` and have the following code:

```python

from solution import awesome_sum
import unittest

class AwesomeSumTest(unittest.TestCase):
    def test_one_plus_one(self):
        self.assertEqual(2, awesome_sum(1,1))

    # You can add more tests cases here

if __name__ == '__main__':
    unittest.main()

```

And after this, just call:

```
$ py awesome_sum_tests.py
....
----------------------------------------------------------------------
Ran 1 tests in 0.000s

OK
```

And you are one step closer from test-driven development.
