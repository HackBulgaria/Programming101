# Zoo Problem - Simulating a zoo


## We'll be writing a program that will simulate the live going on in the zoo.

Here are descriptions of the classes you should have to complete the task, but
of course you're free to add more if you feel you'll need to.

There is also a database file that has a table with possible animals, which
you should use too ^^


## Animal class should have the following attributes:

* species
* age
* name - __This must be unique.__ (Because zoo animals have names! )
* gender
* weight

## An animal can to the following things:

* it can grow (increase it's weight and age)
* it can eat (consume food)
* it can die (The close the animal gets to its life expectancy, the higher the chance of dying)

## Chance of dying

To calculate the chance of dying, take the ratio of the current age of the animal and divide it by the life expectancy for the given specie:

```
chance_of_dying = current_animal_year / life_expectancy
```

## Zoo class should have:

* animals, of course
* capacity (how many animals can it accommodate)
* budget (the money it has at the moment)

## A zoo can do the following thins:

* The zoo can accommodate an animal
* It has daily incomes depending on how much animals it has (the more animals it has, the more interesting it will be to go into that zoo, right?)
* It has daily outcomes depending on how much do the animals eat (every food has it's price)
* Sadly, animals can die in the zoo :/
* The animals reproduce half an year (6 months) after their gestation period is over.

## How an animal is born

* If a male and a female of the same species are present,
after gestation period a new animal is born.
* After an animal is born, after 6 months the female is ready
to reproduce again.
* There's only one baby animal __which gender is 50/50 chance__ to be male or female.

## Costs of accomodating an animal

* an animal brings 60$ back to the zoo per day
* one kilo meat costs 4$
* one kilo grass, foliage or bamboo costs 2$

## We wrote for you a database with animals

You can open the ```animals.db``` file with sqlite browser!

__The data in that table is very important!__

The table contains the following columns:
* species (for example, a tiger)
* life expectancy - how long is the species expected to live
* food type - a carnivore (eats meat) or a herbivore (eats grass, etc.)
* gestation period - how long does the female carry the baby (in months)
* newborn and average weight (in kilos)
* weight/age ratio - how much does the species grow for a month 'till average weight
(when the species gets to average weight, it stops growing)
* food/weight ratio - how much does the species eat (in kilos) per weight (also in kilos)

__The ages in the table are in months__


## The program, simulating a zoo

We can have a lots of Zoos, but for the simulation, we are going to create one Zoo when the program starts and work with it.

You should have the following interface to communicate with the written program:

`see_animals`- prints all animals in the zoo in the following format: `<name> : <species>, <age>, <weight>`

`accommodate <species> <name> <age> <weight>` - adds an animal to the zoo

`move_to_habitat <species> <name>` - removes an animal from the zoo and returns it to it's natural habitat

`simulate <interval_of_time> <period>` where:
`<interval_of_time>` is 'days', 'weeks', 'months' or 'years' and `<period>` is a number.

For every `<interval_of_time>` the program should print the current state of the zoo:

* list the animals stats (in the format above)
* prints if an animal has died
* prints if an animal has been born
* prints if the zoo doesn't have enough budget to pay for the food

Good luck!

And don't forget the three things we're trying to code with:
* test driven development
* objected oriented programming
* databases
