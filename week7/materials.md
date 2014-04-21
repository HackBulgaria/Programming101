# ORM with SQLAlchemy

For the final week of the course, we are going to deal with ORM and the [Python library SQLAlchemy](http://www.sqlalchemy.org/)!

The best way to get started with SQLAlchemy is to watch the video and follow the materials from here: http://www.sqlalchemy.org/library.html#introductiontosqlalchemy

There are slides and code examples too!

## Step by step, working with SQLAlchemy

We are going to take it slow and work step by step with the ORM.

### Install

To install SQLAlchemy, we are going to use pip. __Don't forget to create virtualenv for your project!__

```
pip install SQLAlchemy
```

This should install the latest version (Which is 0.9.4 by the time of writing this)


### Getting around the ORM system

We will start with a small chunk of Python code, that will create a table, called `student` and map it to `Student` class.

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

# A class that maps to a table, inherits from Base
Base = declarative_base()


# Our class will be mapped to a table with name student
# Each field is a Column with the given type and constraints
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)
```

If we run this program, lets call it `orm.py`:

```
$ python orm.py
$ ls
orm.py env university.db
```

We are going to see that `university.db` was created.

If we open the file with `sqlite3` and ask for `.tables`:

```
$ sqlite3 university.db
SQLite version 3.7.9 2011-11-01 00:52:41
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
student
```

We will see that student table was created.

### Adding new record to our database

Lets change `orm.py` to the following code:

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)

# Session is our Data Mapper
session = Session(bind=engine)

print("Adding new student to the database via the session object")
student1 = Student(name="Rado", age=23)
session.add(student1)
session.commit()
```

Now if we run the script and check our database:

```
$ python orm.py
Adding new student to the database via the session object
$ sqlite3 university.db
SQLite version 3.7.9 2011-11-01 00:52:41
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> select * from student;
1|Rado|23
```

### Adding multiple records & querying them

Lets add 3 students and query back to display them.

This is achieved by the following transformation of `orm.py`:

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)

# Session is our Data Mapper
session = Session(bind=engine)

print("Adding new student to the database via the session object")
session.add_all([
    Student(name="Rado", age=23),
    Student(name="Ivo", age=21),
    Student(name="Ivan", age=23)])


# SELECT * FROM student;
all_students = session.query(Student).all()
# list of Student objects
print(all_students)
```

Now if we run the program:

```
$ python orm.py
Adding new student to the database via the session object
[1 - Rado, 2 - Ivo, 3 - Ivan]
```

This is a list of Student objects, but we have `__str__` and `__repr__` implemented.

### More on queyring - WHERE statement via filter

Lets have the following `orm.py`:

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)

# Session is our Data Mapper
session = Session(bind=engine)

print("Adding new student to the database via the session object")
session.add_all([
    Student(name="Rado", age=23),
    Student(name="Ivo", age=21),
    Student(name="Ivan", age=23)])


# SELECT * FROM student WHERE name = "Rado";
rado = session.query(Student).filter(Student.name == "Rado").all()
print(rado)

# SELECT name, age FROM student WHERE age = 23
twenty_three = session.query(Student.name, Student.age).\
    filter(Student.age == 23).all()

for student in twenty_three:
    print("Name {} with age {}".format(student.name, student.age))
```

If we run the program, we will get the following output:

```
$ python orm.py
Adding new student to the database via the session object
[1 - Rado]
Name Rado with age 23
Name Ivan with age 23
```

### We call it relationship. And we build it with Foreign Keys!

Now, we are going to introduce another class (table), called Grade.

We will keep many grades for our students. The relationship here is:

* 1 student has many grades.
* Many grades can be assigned to one student

We will introduce foreign key, when creating the new class:

```python
# One student can have many grades
# So we will have one-to-many relationship here
class Grade(Base):
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("Student", backref="grades")
```

Here is the entire program. Don't forget to remove `university.db` before running.

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship


Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


# One student can have many grades
# So we will have one-to-many relationship here
class Grade(Base):
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("Student", backref="grades")

engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)

# Session is our Data Mapper
session = Session(bind=engine)

print("Adding new student to the database via the session object")
session.add_all([
    Student(name="Rado", age=23),
    Student(name="Ivo", age=21),
    Student(name="Ivan", age=23)])


# SELECT * FROM student WHERE name = "Rado";
rado = session.query(Student).filter(Student.name == "Rado").one()

# Now, lets add some grades to rado:

rado.grades = [Grade(value=6), Grade(value=5), Grade(value=3)]
session.commit()

# And add grades to ivo

ivo = session.query(Student).filter(Student.name == "Ivo").one()
ivo.grades.append(Grade(value=6))

# And now, lets see the avg of grades of Rado:
from sqlalchemy import func

avg_grades = session.query(func.avg(Grade.value)).\
    filter(Student.id == ivo.id).\
    one()
print(avg_grades)

```
