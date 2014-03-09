Problems with files :)

Working with files in Python is easy. We are going to do a bunch of problems to illustrate the concept.

But first, some API:

__Reading files__:

Lets have two files:

* read.py - the python script
* file.txt - the file we want to read

```python
# read.py


filename = "file.txt"
file = open(filename, "r") # Here, "r" stands for open for reading

# file is a file object
# to get all the content:

content = file.read()
print(content)

# when we are done, we close the file
file.close()
```

If we want to iterate on every line, we can do the following:

```python
for line in file:
    print(line)
```

Each line ends up with a special character, called line break - ```\n```.
In order to get each line as an element of a list, you can do the following:

```python
contents = file.read().split("\n")
```

__Writing files:__

Writing to files is just as easy:

```python
# write.py


filename = "file.txt"
file = open(filename, "w") # Here, "w" stands for open for writing

contents = ["Python is awesome.", "You should check it out!"]

# Here, we are joining each element with a new line
file.write("\n".join(contents))

# when we are done, we close the file
file.close()
```

Now, if we run the following program:

```$ python write.py```

and check what's in ```file.txt```:

```
$ cat file.txt
Python is awesome.
You should check it out!
```

We will see our content!

__File arguments:__

When we run our python scripts with ```$ python script.py```, ```script.py``` is an argument to the python program.

We can do the same thing with our python scripts:

```$ python cat.py file.txt```

Here, for example, file.txt is an argument to the cat.py script.

The simplest way to get your arguments is the following:

```python
# argv.py
import sys

for arg in sys.argv:
    print(arg)
```

Now, if we run the following command on the shell, we will see the output

```
$ py argv.py hello.txt program.py script.py
argv.py
hello.txt
program.py
script.py
```

__IMPORTANT:__ The first argument is always the file name!


## Problem F1 - Implement the cat command - Print file contents

In linux, there is a very useful command, called ```cat```:

```
$ cat file.txt
This is some file
And cat is printing it's contents
```

Implement a Python script, called ```cat.py``` that takes one argument - a filename and prints the contents of that file to the console.

### Boilerplate

```python
# cat.py
import sys


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

If we have ```file.txt``` in the same directory with ```cat.py```, and ```file.txt``` is with the following text:

```
Python is an awesome language!
You should try it.
```

This is the result:
```
$ python cat.py file.txt
Python is an awesome language!
You should try it.
```

## Problem F2 - Cat multiple file

Implement a Python script, called ```cat2.py``` that takes multiple arguments - file names and prints the contents of all files to the console, in the order of the arguments.

__The number of the files that are given as arguments is unknown.__

There should be a newline between every two files that are printed.

### Boilerplate

```python
# cat2.py
import sys


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

If we have two files - ```file1.txt``` and ```file2.txt``` in the same directory with ```cat2.py``` and:

__file1.txt:__
```
Python is an awesome language!
You should try it.
```

__file2.txt:__
```
Also, you can use Python at a lot of different places!
```


This is the result:
```
$ python cat2.py file1.txt file2.txt
Python is an awesome language!
You should try it.

Also, you can use Python at a lot of different places!
```

## Problem F3 - Generate file with random integers

Implement a Python script, called ```generate_numbers.py``` that takes two arguments - a ```filename``` and an integer ```n```.

The script should create a file with the ```filename``` and print ```n``` random integers, separated by ```" "```

For random integers, you can use:

```python
from random import randint
print(randint(1, 1000))
```

### Boilerplate

```python
# generate_numbers.py
import sys
from random import randint


def main():
    pass

if __name__ == '__main__':
    main()
```

### Examples

```
$ python generate_numbers.py numbers.txt 100
$ cat numbers.txt
612 453 555 922 120 840 173 98 994 461 392 739 982 598 610 205 13 604 304 591 830 313 534 47 945 26 975 338 204 51 299 611 699 712 544 868 2 80 472 101 396 744 950 561 378 553 777 248 53 900 209 817 546 12 920 219 38 483 176 566 719 196 240 638 812 630 315 209 774 768 505 268 358 39 783 78 94 293 187 661 743 89 768 549 106 837 687 992 422 30 897 174 844 148 88 472 808 598 341 749
```

## Problem F4 - Sum integers from file

Implement a Python script, called ```sum_numbers.py``` which takes one argument - a ```filename``` which has integers, separated by ```" "```

The script should print the sum of all integers in that file.

### Examples

If we use the generated file from Problem 3:

```
$ python sum_numbers.py numbers.txt
47372
```

## Problem F5 - Concatenate files into one

Implement a Python script, called ```concat_files.py``` that takes multiple filenames as arguments.

The script should concatenate all file contents into a single file, called ```MEGATRON``` (Capslock is by choice :D)

Every time you run the script, do not delete the old contents of ```MEGATRON``` but append the new ones at the end of the file.

### Examples

Again, let's have the following files:

__file1.txt:__
```
Python is an awesome language!
You should try it.
```

__file2.txt:__
```
Also, you can use Python at a lot of different places!
```

Running the script:

```
$ python concat_files.py file1.txt file2.txt
$ cat MEGATRON
Python is an awesome language!
You should try it.

Also, you can use Python at a lot of different places!
$ python concat_files.py file1.txt file2.txt
$ cat MEGATRON
Python is an awesome language!
You should try it.

Also, you can use Python at a lot of different places!

Python is an awesome language!
You should try it.

Also, you can use Python at a lot of different places!
```

## Problem F6 - Count characters, words or lines

Implement a Python script, called ```wc.py``` that takes two arguments:

* A command, that can be one of the following : ```chars```, ```words```, ```lines```
* A filename

The script should output, according to the command, the following:

* For the command ```chars```, the number of characters in the file
* For the command ```words```, the number of words in the file
* For the  command ```lines```, the number of lines in the file


### Examples

Lets have the following text:

__story.txt:__

```
Now indulgence dissimilar for his thoroughly has terminated. Agreement offending commanded my an. Change wholly say why eldest period. Are projection put celebrated particular unreserved joy unsatiable its. In then dare good am rose bred or. On am in nearer square wanted.

Of resolve to gravity thought my prepare chamber so. Unsatiable entreaties collecting may sympathize nay interested instrument. If continue building numerous of at relation in margaret. Lasted engage roused mother an am at. Other early while if by do to. Missed living excuse as be. Cause heard fat above first shall for. My smiling to he removal weather on anxious.

Ferrars all spirits his imagine effects amongst neither. It bachelor cheerful of mistaken. Tore has sons put upon wife use bred seen. Its dissimilar invitation ten has discretion unreserved. Had you him humoured jointure ask expenses learning. Blush on in jokes sense do do. Brother hundred he assured reached on up no. On am nearer missed lovers. To it mother extent temper figure better.

```

__Print the chars:__

```
$ python wc.py chars story.txt
1032
```

__Print the words:__

```
$ python wc.py words story.txt
166
```

__Print the lines:__

```
$ python wc.py lines story.txt
6
```

## Problem F7 - Pizza delivery

Implement a Python program, called ```pizza.py``` that will help us organize the pizza ordering!

We are going to implement a program, that waits for commands from the user and acts on them. Some commands may affect other commands and the program loops forever, until ```finish``` command is issued.

We are going to take input in Python like that:

```python
command = input("Enter command>")
```

Here is an example start of the program:

```
$ python pizza.py
Enter command>
```

The user can enter one of the following commands:

* ```take <name> <price>```
* ```status```
* ```save```
* ```list```
* ```load <number>  ```
* ```finish```

Now let's go through each of the commands:

__take <name> <price>__

The take commands followed by a name and a price, adds the given Person with the given prices to the current order.

One person can take many things, adding up to the total price for him.

For example:

```
Enter command>take Rado 10.0
Taking order from Rado for 10.00
Enter command>take Rado 10
Taking order from Rado for 10.00
Enter command>take Ivan 6.43
Taking order from Ivan for 6.43
Enter command>take Maria 7.50
Taking order from Maria for 7.50
Enter command>
```

__status:__

The status command prints the current status of the order in the following format for each person:

```
Person - Total Sum
```

For example:

```
Enter command>take Rado 10.0
Taking order from Rado for 10.00
Enter command>take Rado 10
Taking order from Rado for 10.00
Enter command>take Ivan 6.43
Taking order from Ivan for 6.43
Enter command>take Maria 7.50
Taking order from Maria for 7.50
Enter command>status
Rado - 20.00
Ivan - 6.43
Maria - 7.50
Enter command>
```

__save:__

We should be able to save the current order in a file!

When we issue the ```save``` command, the script should do the following:

* Create a timestamped file, named ```orders_YYYY_mm_dd_hh_mm_ss``` where ```YYYY``` is the current year, ```mm``` the current month, ```dd``` the current day, ```hh``` the current hour, ```mm``` the current minutes and ```ss``` the current seconds.

You can achieve the timestamp with the following code:

```python
from time import time
from datetime import datetime

ts = time()
stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
```

* Save the current order in that file. The formating of the current order should be the same formatting, when printing it with the ```status``` command.

* After the file is saved, keep taking orders (Don't quit the program)

__list:__

The list command shows all files with saved orders in the current directory.

When displaying them, it adds unique number to each file, starting from one. This number will be used in the ```load``` command.

See this example, where we do two saves and call ```list``` after that:

```
Enter command>take Ivan 10
Taking order from Ivan for 10.00
Enter command>take Maria 5.50
Taking order from Maria for 5.50
Enter command>take Rado 6.10
Taking order from Rado for 6.10
Enter command>save
Saved the current order to orders_2014_03_01_11_00_00
Enter command>take Maria 10.50
Taking order from Maria for 10.50
Enter command>save
Saved the current order to orders_2014_03_01_11_00_08
Enter command>list
[1] - orders_2014_03_01_11_00_08
[2] - orders_2014_03_01_11_00_00
Enter command>

```

__load <number>:__

The load command discards the current order and loads a saved one from a file. A second argument, a number, is given. This is the unique number for the file, showed in the ```list``` command.

The algorithm for load is:

* If you call ```load``` before ```list```, a message is displayed : ```Use list command before loading```
* If you load a file and the current order is not saved (Changes have been made after the last save or no save at all) - The program should display a warning message :

```
You have not saved the current order.
If you wish to discard it, type load <number> again.
```
* If you type ```load <number>``` again, the current order is discarded and it's replaced by the one saved in the file. You have to parse the file for that.

* If you call ```load``` and you have an empty current order, you should load the file without a problem.

__Check the examples:__


Loading without save:
```
Enter command>take Rado 10
Taking order from Rado for 10.00
Enter command>take Maria 5.50
Taking order from Maria for 5.50
Enter command>list
[1] - orders_2014_03_01_11_00_08
[2] - orders_2014_03_01_11_00_00
Enter command>load 1
You have unsaved order.
If you wish to discard the current order, type load again
Enter command>
```


Loading order:

```
$ cat orders_2014_03_01_11_00_00
Maria - 5.50
Ivan - 10.00
Rado - 6.10%
```

```
$ py pizza.py
Enter command>list
[1] - orders_2014_03_01_11_00_08
[2] - orders_2014_03_01_11_00_00
Enter command>load 2
Loading orders_2014_03_01_11_00_00
Enter command>status
Maria - 5.50
Rado - 6.10
Ivan - 10.00
Enter command>

```

__finish:__

The ```finish``` command is for exiting the program.

Here is the algorithm for ```finish```:

* If you type finish and you have unsaved changes, you will get the following message:

```
Enter command>finish
You have not saved your order.
If you wish to continue, type finish again.
If you want to save your order, type save
```

* If you type finish again, the program will exit

```
Enter command>finish
Finishing order. Goodbye!
$
```

__unknown command:__

If you type a command that is not supported by the program, print an error message.

Something like this:

```
Enter command>OMG
Unknown command!
Try one of the following:
take <name> <price>
status
save
list
load <number>
finish
Enter command>

```
