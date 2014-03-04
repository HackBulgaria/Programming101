A bunch of simple problems, to warm up with Python. Those are the regular programming problems, that you meet in every beginners course.

The solutions should be written for Python 3.* version.


## Problem 0 - Students Attendance

Implement a Python program, called ```attendance.py``` that will help us organize our course.

We are going to implement a program, that waits for commands from the user and acts on them. Some commands may affect other commands and the program loops forever, until ```finish``` command is issued.

First of all, we have a text file, called ```students``` which holds all students, attending the course. This will be our database.

[You can find the students file in the same week1 directory in Github.](https://github.com/HackBulgaria/Programming101/blob/master/week1/students)
Your program is working with the given students.

Here is an example start of the program:

```
$ python attendance.py
Enter command>
```

The user can enter one of the following commands:

* ```create```
* ```change_date``` <date>
* ```add <name>```
* ```list```
* ```load```
* ```status```
* ```statistics```

Now let us go through each of the commands:

__create__

The purpose is to create a file, to store attendance for the given day.

It creates a new database file with name ``` attendance_YYYY_mm_dd``` where ```YYYY``` is the current year, ```mm``` the current month, ```dd``` the current day.

After creating a new file, it automatically loads it. Now you can use the ```add``` command.

The commands return the following output:

```
New file created and loaded: attendance_2014_03_01
```

__If you already have a file for the current date you must see that error:__

```
Enter command>create
New file created and loaded: attendance_2014_03_01
Enter command>create
You already have a file for today it is: attendance_2014_03_01
```

__change_date__

With this command, we can change the current date and create new file.
Here is an example:

```
Enter command> change_date 02/03/2014
Date changed to 02/03/2014.
Current file saved & discarded.
You can create or load.
```

The format of the date is ```DD/MM/YYYY```

After changing the date, discard the currently created file. The user can now create new one for the given date or load an old file.

__add__

```
Enter command>add Rado
Rado is now attending
Enter command>add Ivo
Ivo is now attending
```

__In order to add someone to the attendance file, he must be present in the ```students``` file!__

If you try adding someone two times, the program should notify you:

```
Enter command>add Rado
Rado is now attending
Enter command>add Rado
Rado is already added to the list for today.
```

Everytime you add a new person, the file should be saved.

__list__

These command list all attendance files in current directory.

```
Enter command>create
New file created and loaded: attendance_2014_03_01
Enter command>add Ivo
Ivo is now attending
Enter command>add Rado
Rado is now attending
Enter command>list
[1] - orders_2014_03_01
[2] - orders_2014_03_02
```

__load__

This is the command that loads files. It takes one argument [File ID]. That id is taken form the ```list``` command.

```
Enter command>list
[1] - orders_2014_03_01
[2] - orders_2014_03_02
Enter command>load 1
File orders_2014_03_01 loaded
```

If you load an old attendance file, you can still add people to it.


__status__

This command shows lists all people that you have added in the current file.

```
Enter command>create
New file created and loaded: attendance_2014_03_01
Enter command>add Ivo
Ivo is now attending
Enter command>add Rado
Rado is now attending
Enter command>add Frodo
Frodo is now attending
Enter command>add Bat Georgi
Bat Giorgi is now attending
Enter command>status
Ivo
Rado
Frodo
Bat Georgi
```

You can status a loaded file:

```
Enter command>list
[1] - attendance_2014_03_01
Enter command>load 1
File attendance_2014_03_01 loaded
Enter command>status
Ivo
Rado
Frodo
Bat Georgi
```

__statistic__

The commands shows all dates and the amount of people attending for each day, compared to the total amount of people in ```students```

```
Enter command>statistic
File: 2014-03-01 - 4 people attending from total of 45 students
File: 2014-03-02 - 5 people attending from total of 45 students
```
