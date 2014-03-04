A bunch of simple problems, to warm up with Python. Those are the regular programming problems, that you meet in every beginners course.

The solutions should be written for Python 3.* version.


## Problem 0 - Students Attendance

Implement a Python program, called ```attendance.py``` that will help us organize our course.

We are going to implement a program, that waits for commands from the user and acts on them. Some commands may affect other commands and the program loops forever, until ```finish``` command is issued.

First of all, we have a text file, called ```students``` which holds all students, attending the course. This will bne our database.

Here is an example start of the program:

```
$ python attendance.py
Enter command>
```

The user can enter one of the following commands:

* ```create```
* ```add <name>```
* ```list``` 
* ```load```
* ```status```
* ```statistics```

Now let us go through each of the commands:

__create__

It creates a new database file with name ``` attendance_YYYY_mm_dd_hh_mm_ss ``` where ```YYYY``` is the current year, ```mm``` the current month, ```dd``` the current day, ```hh``` the current hour, ```mm``` the current minutes and ss the current seconds.

After creating a new file, it automatically loads it. Now you can use the ```add``` command.

The commands return the following string:
```
New file created and loaded: attendance_2014_03_01_11_00_00
```
__If you already have a file for the current date you must see these error__

```
Enter command>create
New file created and loaded: attendance_2014_03_01_11_00_00
Enter command>create
You already have a file for today it is: attendance_2014_03_01_11_00_00
```

__add__

```
Enter command>add Rado
Rado is now attending
Enter command>add Ivo
Ivo is now attending
```

These command adds the persons name into the file. Now the persons in attending our course. You cant add people without __creat__-ing or __load__-ing a file.

__list__

These command list all files in current directory

```
Enter command>create
New file created and loaded: attendance_2014_03_01_11_00_00
Enter command>add Ivo
Ivo is now attending
Enter command>add Rado
Rado is now attending
Enter command>list
[1] - orders_2014_03_01_11_00_08
[2] - orders_2014_03_01_11_00_00
```

__load__ 

This is the command that loads files. It takes one argument [File ID]. That id is taken form the list command.

```
Enter command>list
[1] - orders_2014_03_01_11_00_08
[2] - orders_2014_03_01_11_00_00
Enter command>load 1
File orders_2014_03_01_11_00_08 loaded
```


__status__

This command shows lists all people that you have added in the current file.

```
Enter command>create
New file created and loaded: attendance_2014_03_01_11_00_00
Enter command>add Ivo
Ivo is now attending
Enter command>add Rado
Rado is now attending
Enter command>add Frodo
Frodo is now attending
Enter command>add Bat Giorgi
Bat Giorgi is now attending
Enter command>status
Ivo
Rado
Frodo
Bat Giorgi
```

You can status a loaded file:

```
Enter command>list
[1] - attendance_2014_03_01_11_00_00
Enter command>load 1
File attendance_2014_03_01_11_00_00 loaded
Enter command>status
Ivo
Rado
Frodo
Bat Giorgi
```

__statistic__

The commands lists shows all dates and the amount of people attending

```
Enter command>statistic
File: 2014-03-01 - 4 people attending
File: 2014-03-02 - 5 people attending
```
