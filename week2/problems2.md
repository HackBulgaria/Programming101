We are going to do some basic OOP problems, mixed with unit testing and TDD!

In order to skip the long explanation that can be showed with code, we will jump to the problems.

__When implementing the classes, use the TDD technique!__

## Problem 0 - A hero.

So lets start with something simple. We are going to implement a hero class, step by step.

Implement a class, that represents a hero. Our hero is going to start simple:

* Our hero has a ```name``` attribute
* Our hero has a ```health``` attribute
* Our hero has a ```nicknamе``` attribute

If our hero is implemented in ```hero.py```, here is a simple usage in the __python interpreter__:

```
>>> import hero
>>> h = hero.Hero("Bron", 100, "DragonSlayer")
>>> h
<hero.Hero object at 0x7f5aa39c30d0>
>>> h.name
'Bron'
>>> h.nickname
'DragonSlayer'
>>> h.health
100
```
### known_as() method

Add a ```known_as()``` method to our Hero, which returns a string, formatted in the following way:
```hero_name the hero_nickname```

__For example:__

```
>>> h.known_as()
Bron the DragonSlayer
```

### get_health()

Every hero starts with the given ```health```.

__This ```health``` is the maximum health for the hero!__

When a hero reaches 0 ```health``` he is considered death.

Add this attribute to our hero and implement the following methods:

* ```is_alive()``` which returns True, if our hero is still alive. Otherwise - False.
* ```get_health()``` which returns the current health

### take_damage(damage_points)

So, our hero can take damage which reduces his health.

Implement a method, called ```take_damage(damage_points)``` where damage can be either integer or floating point value.

This method should reduce the hero's health by ```damage```

__If we inflict more damage than we have health, health will always be equal to zero and we cannot get below that!__

### take_healing(healing_points)

Our hero can also be healed!

Implement a method, called ```take_healing(healing_points)``` which heals our hero.

Here are the requirements:

* If our hero is dead, the method should return False. It's too late to heal our hero
* We cannot heal our hero above the maximum health, which is given by ```health```
* If healing is successful (Our hero is not dead), the method should return True

## Problem 1 - The Orc.

In order to have a world of heroes, we must have a world of villains and bad guys.

But this time, we are going one level up - we are having orcs!

In ```orc.py```, implement an Orc class with the following attributes, given to the constructor

* ```name``` - every orc has a name! A terrifying name.
* ```health``` - unlike our hero, every Orc starts with a different level of health
* ```berserk_factor``` - a floating point number between 1 and 2. This factor is used, when the Orc goes berserk! (If a factor, larger than 2 or smaller than 1 is given, it is bounded by the limit (1 or 2))

Just like our hero, the orc has the same methods for healing, damage and life status:

* get_health()
* is_alive()
* take_damage(damage_points)
* take_healing(healing_points)

## Problem 2 - The Entity? Time to do some refactoring

If we take a look at our Hero and our Orc, they have few things in common:

* name
* health
* get_health()
* is_alive()
* take_damage(damage_points)
* take_healing(healing_points)

The OOP approach can save us some of the code repetition by doing inheritance.

Create a class, called ```Entity``` which shares all the common things between a hero and an orc.

After this, refactor your code and tests, in order to inherit from that Entity and still maintain the specific methods for each class.

If you want to call a superconstructor, you can do it like so:

```python
from entity import Entity


class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
    # ...
```

Refactor your tests as well, so everything can pass!

### Problem 3 - The Weapon!

We are going to make an army of heroes and an army of orcs and make them fight!
But first, we are going to need some weapons.

Create a class ```Weapon```, which takes the following attributes as a constructor:

* ```type``` - a string that represents the weapon. Imagine an axe!
* ```damage``` - how many health points you are going to take away, if you hit!
* ```critical_strike_percent``` - a floating number between 0 and 1 that gives the chance for double damage!

Implement a method, called ```critical_hit()``` which returns True, if the weapon, striking now, should do 2x times the damage, according to the ```critical_strike_percent```.

Otherwise, False

__Example__:

```
>>> from weapon import Weapon
>>> axe = Weapon("Mighty Axe", 25, 0.2)
```

### Problem 4 - Equipping some weapons

It's time to Equip our fighters.

In the ```Entity``` class, add the following methods:

* ```has_weapon()``` - return True, if the given Entity is already equipped with a weapon
* ```equip_weapon(weapon)``` - equips the given weapon to the Entity. If you equip a new weapon, the old one is discarded.
* ```attack()``` - return the damage, that the given Entity is doing. If the entity has no weapon, the damage is 0

In the ```Orc``` class, __override__ the ```attack()``` method to take into account the ```berserk_factor``` !

### Problem 5 - A class for Fighting

Now, it is time to make them fight!

Implement a class ```Fight``` which takes two arguments to the constructor:

* A ```Hero``` instance
* An ```Orc``` instance

The ```Fight``` class flips a coin and decides which will attack first. (Imagine, take random between 0 and 100. If it is < 50, hero attacks first, else orc attacks first)

Implement a ```simulate_fight()``` method, which starts a fight between the hero and the orc, and prints out the status of the battle to the console.

The fight ends, when either the hero or the orc dies!

### Problem 6 - Inside the dungeon

Now, when we can fight our Hero and our Orc, it's time to make an adventure!

But first, lets go step by step. Implement a class ```Dungeon```, that loads a dungeon map from a text file.

The file path should be given as the only argument to the constructor.

A dungeon, looks something like this:

```
S.##......
#.##..###.
#.###.###.
#.....###.
###.#####S
```

Where:

* ```S``` means a starting point - you can spawn there.
* ```#``` is an obstacle - you cannot go there
* ```.``` is a walkable path - you can follow the dots.

For example, lets have a file, called ```basic_dungeon.txt``` which represents the dungeon above.

We create new dungeon like this:

```
>>> from dungeon import Dungeon
>>> map = Dungeon("basic_dungeon.txt")
>>> map.print_map()
S.##......
#.##..###.
#.###.###.
#.....###.
###.#####S
```

For now, implement a method, called ```print_map()``` which prints the map to the output, in a formatted way.


### Problem 7 - It's spawning time.

This one goes for the bonus round. If someone reaches here, notify me!
