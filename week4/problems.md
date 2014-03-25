## Problem 0 - SQLite Database Browser & Polyglot

We are going to start with a GUI (Graphical User Interface) tool, for managing sqlite - just to see that the things are working correctly!

If you are using Ubuntu, you can install [SQLite Database Browser](https://apps.ubuntu.com/cat/applications/sqlitebrowser/), which is simple enough for our needs!

Now, go back to the [Polyglot repository](https://github.com/HackBulgaria/Polyglot), and locate the ```polyglot.db``` file and open it in the SQLite Database Browser!

When the file is loaded, take a look at the tables.

## Problem 1 - sqlite3 shell tool

Now, back to the console.

__First, check if you have the tool for running sqlite3 shell client, by typing:__

```
$ sqlite3
```

If you see:

```
SQLite version 3.7.9 2011-11-01 00:52:41
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

Everything is OK! If there is an error, you should install ```sqlite3```:

```
sudo apt-get install sqlite3 libsqlite3-dev
```

Now, navigate to the ```Polyglot``` directory and call the following command:

```
$ sqlite3 polyglot.db
```

And run the following SQL statement:

```
sqlite>SELECT * FROM languages;
```

You will get the following result:

```
1|Python|google|0|A folder named Python was created. Go there and fight with program.py!
2|Go|200 OK|0|A folder named Go was created. Go there and try to make Google Go run.
3|Java|object oriented programming|0|A folder named Java was created. Can you handle the class?
4|Haskell|Lambda|0|Something pure has landed. Go to Haskell folder and see it!
5|C#|NDI=|0|Do you see sharp? Go to the C# folder and check out.
6|Ruby|https://www.ruby-lang.org/bg/|0|Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!
7|C++|header files|0|Here be dragons! It's C++ time. Go to the C++ folder.
8|JavaScript|Douglas Crockford|0|NodeJS time. Go to JavaScript folder and Node your way!
sqlite> SELECT * FROM languages;
1|Python|google|0|A folder named Python was created. Go there and fight with program.py!
2|Go|200 OK|0|A folder named Go was created. Go there and try to make Google Go run.
3|Java|object oriented programming|0|A folder named Java was created. Can you handle the class?
4|Haskell|Lambda|0|Something pure has landed. Go to Haskell folder and see it!
5|C#|NDI=|0|Do you see sharp? Go to the C# folder and check out.
6|Ruby|https://www.ruby-lang.org/bg/|0|Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!
7|C++|header files|0|Here be dragons! It's C++ time. Go to the C++ folder.
8|JavaScript|Douglas Crockford|0|NodeJS time. Go to JavaScript folder and Node your way!
```

## Problem 2 - Tables, tables everywhere! SELECT, UPDATE, INSERT, DELETE

Now, we know that our languages table looks like this:

| id      | language  | answer  | answered | guide |
| ------------- |:-------------:| --- | --- |-----:|
1|Python|google|0|A folder named Python was created. Go there and fight with program.py!
2|Go|200 OK|0|A folder named Go was created. Go there and try to make Google Go run.
3|Java|object oriented programming|0|A folder named Java was created. Can you handle the class?
4|Haskell|Lambda|0|Something pure has landed. Go to Haskell folder and see it!
5|C#|NDI=|0|Do you see sharp? Go to the C# folder and check out.
6|Ruby|https://www.ruby-lang.org/bg/|0|Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!
7|C++|header files|0|Here be dragons! It's C++ time. Go to the C++ folder.
8|JavaScript|Douglas Crockford|0|NodeJS time. Go to JavaScript folder and Node your way!


A ```SELECT``` statement, returns a list of rows. We ```SELECT``` by giving the name of the columns we want.

Run the following SELECT statements in the sqilite3 shell:

1.
```sql
SELECT id FROM languages;
```
2.
```sql
SELECT id, language FROM languages;
```
3.
```sql
SELECT id, language, answer, answered FROM languages;
```
4.
```sql
SELECT id, language FROM languages WHERE answered = 0;
```
5.
```sql
SELECT id, language FROM languages WHERE answered = 1;
```

__Now, lets update few languages to be answered. We will change the answered value for each language from 0 to 1:__

1.
```sql
UPDATE languages SET answered = 1 WHERE language = "Python";
```
2.
```sql
SELECT id, language FROM languages WHERE answered = 1;
```

Now, if we run the ```polyglot.py``` program and give the ```list``` command, we will see:

```
DONE [1] - Python
NOT_DONE [2] - Go
NOT_DONE [3] - Java
NOT_DONE [4] - Haskell
NOT_DONE [5] - C#
NOT_DONE [6] - Ruby
NOT_DONE [7] - C++
NOT_DONE [8] - JavaScript
```

As you can see, if we control the data, we control the program!

__Now, let's insert a new language in our table!__

Execute the following statements:

*
```sql
INSERT INTO languages(id, language, answer, answered, guide) VALUES(9, "PHP", "$$$", 0, "Can you handle this piece of PHP?");
```
*
```sql
SELECT language FROM languages;
```

Now, if we go to our Polyglot program, again, we will see that PHP was added too:

```
DONE [1] - Python
NOT_DONE [2] - Go
NOT_DONE [3] - Java
NOT_DONE [4] - Haskell
NOT_DONE [5] - C#
NOT_DONE [6] - Ruby
NOT_DONE [7] - C++
NOT_DONE [8] - JavaScript
NOT_DONE [9] - PHP
```

Now, to finish the cycles of SQL statements, we are going to ```DELETE``` the added PHP language

We can achieve that by running the following query:

```sql
DELETE FROM languages WHERE language = "PHP";
```

Now, if we run:

```sql
SELECT language FROM languages;
```

We wont see PHP!

### SUID = CRUD

We were talking about CRUD operations - Create, Read, Update, Delete of a given object.

If we take a look at the SQL query statements, we can relate:

* ```SELECT``` = Read
* ```UPDATE``` = Update
* ```INSERT``` = Create
* ```DELETE``` = Delete

## Problem 3 - A simple Python Script to query the Polyglot database

Copy ```polyglot.db``` to where you work, and create the following script:

```python
import sqlite3

conn = sqlite3.connect("polyglot.db")
cursor = conn.cursor()

result = cursor.execute("SELECT id, language FROM languages")

for row in result:
    print(row)
```

Run the program and see the output!

As you can see, connecting to sqlite is as simple as that!

## Problem 4 - Creating tables with Python

If you see the [following file from the Polyglot problem](https://github.com/HackBulgaria/Polyglot/blob/master/polyglot_creation_script/create_db.py), you will see how a database is created!

Now, implement a Python script, called ```create_company.py``` that creates the following table (Both structure and data):

| id | name  | monthly_salary  | yearly_bonus | position |
| ------------- |:-------------:| --- | --- |-----:|
1|Ivan Ivanov |5000|10000|Software Developer|
2|Rado Rado| 500|0|Technical Support Intern|
3|Ivo Ivo| 10000| 100000| CEO |
4| Petar Petrov | 3000 | 1000 | Marketing Manager|
5| Maria Georgieva | 8000 | 10000 | COO |

After creating the sqlite database, implement a script, called ```manage_company.py``` that can take command input and do the following things:

* On command ```list_employees``` - Prints out all employees, in the following format - "name - position"
* On command ```monthly_spending``` - Prints out the total sum for monthly spending that the company is doing for salaries
* On command ```yearly_spending``` - Prints out the total sum for one year of operation (Again, salaries)
* On command ```add_employee```, the program starts to promt for data, to create a new employee.
* On command ```delete_employee <employee_id>```, the program should delete the given employee from thje database
* On command ```update_employee <employee_id>```, the program should prompt the user to change each of the fields for the given employee
__Here is an example usage:__

```
$ python manage_company.py
command>list_employees
1 - Ivan Ivanov - Software Developer
2 - Rado Rado - Technical Support Intern
3 - Ivo Ivo - CEO
4 - Petar Petrov - Marketing Manager
5 - Maria Georgieva - COO
command>monthly_spending
The company is spending $26500 every month!
command>yearly_spending
The company is spending $439000 every year!
command>add_employee
name>Hristo Hristov
monthly_salary>1200
yearly_bonus>0
position>Junior Software Developer
command>list_employees
command>list_employees
1 - Ivan Ivanov - Software Developer
2 - Rado Rado - Technical Support Intern
3 - Ivo Ivo - CEO
4 - Petar Petrov - Marketing Manager
5 - Maria Georgieva - COO
6 - Ivan Ivanov - Juniour Software Developer
```

```
>delete_employee 6
Ivan Ivanov wasa deleted.
>list_employees
1 - Ivan Ivanov - Software Developer
2 - Rado Rado - Technical Support Intern
3 - Ivo Ivo - CEO
4 - Petar Petrov - Marketing Manager
5 - Maria Georgieva - COO
```

```
>update_employee 2
name>Rado Rado
monthly_salary>1000
yearly_bonus>1000
position>Technical Support
>list_employees
1 - Ivan Ivanov - Software Developer
2 - Rado Rado - Technical Support
3 - Ivo Ivo - CEO
4 - Petar Petrov - Marketing Manager
5 - Maria Georgieva - COO
```
