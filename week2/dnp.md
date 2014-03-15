# Dungeons and Pythons

After building Python skills for 3 weeks, we are going to put everything that we know, into this epic game.

__It is about dungeons and it is about Pythons!__

We are going to simulate a dungeon map, of multiple levels, a hero, that is brave enough to wander through the dungeons, and of course, Pythons, that wait at every corner, for something fresh to eat!

We are going to build a console interface for our game too.

And for all of this, we are going to stick to the TDD approach!

So, enough words. Lets bring the game on!

## The Dungeon

The Dungeon class is responsible for loading the map, taking care of the levels and moving the hero around the map.


### The Map

Here is an example map:

```
S..P..........PPI###############
.#########.#####################
.....P.........................B
.####.##.###.###################
P####.##.###.#####.....#########
.####.##.###.#####.###.##IIIIII#
P####.I..###.#####.###.##P....I#
.####P##P###.......###.##P######
P####.##.############.........B.
I####B...######################G
```

Our maps are going to be represented as a matrix of strings, where each character, means something special:

* ```S``` is the spawning point for our hero. There can be multiple spawning points
* ```P``` is a Python - this is your enemy! Once you step into the Python, you start fighting with him
* ```#``` is an obstacle - you cannot move through it
* ```.``` is a walkable path
* ```I``` is an item - it can be either a new weapon or a healing potion
* ```B``` is a boss enemy - a stronger python, ready to kick our ass
* ```G``` is the Gateway, to the next level

#### Levels

Every game starts from level 1. If the hero reaches the gateway for the given level (Marked by ```G```), the game should load the next level.

You can organize your maps in text files (In a folder called ```maps/```) where every file name is the following: ```level_1.txt```, ```level_2.txt``` etc.

Once you are done with level 1, you load the map for level 2 and spawn the hero there!

__If there are no next levels, the game is over and the hero has won!__

#### Map mechanics

* ```S``` is the spawning point for our hero. There can be multiple spawning points in our map. When spawning a hero, choose one point by random. __Every other Spawning point becomes a walkable path.__
* ```P``` is a Python - this is your enemy! If a hero steps into a Python, this triggers a fight. If our hero dies, the game is over.
* ```I``` is an item - __it can be either a new weapon or a healing potion.__ When a hero steps into it, troll a dice and decide what it should be. Also, pick at random, the attributes of the chosen weapon or a potion.
* ```B``` is a boss. Same as the Python, but stronger.
* ```G``` is the Gateway, to the next level - when a hero steps into this, the next level is loaded.


### Moving the hero around the map

There should be methods, to spawn and move the hero around the map:

#### spawn

```spawn(player_name, hero_instance)``` - spawns a player __at a random spawning point.__

```player_name``` __is a unique string identifier for the player.__ We are going to use ```player_name``` for moving our hero around the map.

__For example:__

```
>>> map.spawn("player_1", some_hero_instance)
>>> map.print_map()
H..!..........PPI###############
.#########.#####################
.....P.........................!
.####.##.###.###################
P####.##.###.#####.....#########
.####.##.###.#####.###.##IIIIII#
P####.I..###.#####.###.##P....I#
.####P##P###.......###.##P######
P####.##.############.........B.
I####B...######################G
```

#### move

Now, implemented a method ```move(player_name, direction)``` where:

* ```player_name``` is the unique identifier for the player
* ```direction``` is ```up```, ```down```, ```left``` and ```right```

This should move the given player in the desired direction.

If you move into a special object - handle the case.

__For example:__
```
>>> map.move("player_1", "right")
.H.!..........PPI###############
.#########.#####################
.....P.........................!
.####.##.###.###################
P####.##.###.#####.....#########
.####.##.###.#####.###.##IIIIII#
P####.I..###.#####.###.##P....I#
.####P##P###.......###.##P######
P####.##.############.........B.
I####B...######################G
```

The method should return False, if the move is not possible (Outside the map or into an obstacle). Otherwise, True

## The Hero

Our hero has the following attributes, that are taken as constructor arguments:

* A ```name``` attribute
* A ```health``` attribute
* A ```nicknamе``` attribute

The given ```health``` is the maximum health our hero can have. He cannot be over-healed!


Once created, our hero starts with 10 damage, that he can do unarmed!

__Our hero always starts unarmed, until he finds a better weapon for fighting.__

The methods for our hero are:

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

Our hero can take damage which reduces his health.

Implement a method, called ```take_damage(damage_points)``` where damage can be either integer or floating point value.

This method should reduce the hero's health by ```damage```

__If we inflict more damage than we have health, health will always be equal to zero and we cannot get below that!__

### take_healing(healing_potion)

Our hero can also be healed!

Implement a method, called ```take_healing(healing_potion)``` which heals our hero.

The healing is done by using a special healing potion, with has an attribute - healing points, by which, our hero is healed.

Here are the requirements:

* If our hero is dead, the method should return False. It's too late to heal our hero
* We cannot heal our hero above the maximum health, which is given by ```health```
* If healing is successful (Our hero is not dead), the method should return True

### equip_weapon(weapon)

Our hero can find a weapon, while wandering around the dungeon. He should be able to equip that weapon!

Once equipped, the weapon makes our hero stronger.

### has_weapon()

Implement the following method for our hero - ```has_weapon()``` - return True, if the given Hero is already equipped with a weapon. Otherwise, False.

### attack()

The main method for our hero! The method for attacking.

This method should return the damaged, that is going to be outputted by our hero.

Take into consideration:

* If our hero is armed or unarmed
* If the weapon is going to make a critical strike

## The Weapon

The tool for war.

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

### Finding weapon on the map

If you find a weapon on the map, and that weapon is better, our hero equips it automatically.

__A weapon is better if it has both better critical strike chance and better damage.__

## The Potion

We are going to have really simple healing potions.

The class for them is going to have only one attribute - ```healing_points``` - a number, by which our hero can be healed.

If our hero finds a healing potion, he automatically drinks it! This item cannot be used during fight.

## The Python

This is our Enemy. A big fat snake, that is going to bite us to death!

Implement a Python class with the following attributes, given to the constructor:

* ```health``` - This is the health of the Python
* ```damage``` - This is the damage points, that the Python is doing when he is attacking.

Implement (or inherit) the following methods, that are doing the same, as in our hero class.

* ```take_damage(damage_points)```
* ```is_alive()```
* ```attack()```

When our Hero steps into a Python, we should start a Fight!

## The Boss

Bosses are stronger Pythons. They are just like the regular python, but with one extra twist:

They accept a third argument, which is a ```berserk_tuple``` of the form ```(4, 1.5)```

The mechanics of the ```berserk_tuple``` is the following:

* The first element is the number of attacks the boss have to make in order to,
* Make a stronger attack, multiplied by the factor (The second tuple element)

This means - every 4th attack, the Boss goes berserk and does more damage (Multiplied by the factor)

__For example:__

Lets have a Boss with __10 damage__ and __berserk tuple - (4, 1.5)__

* Attack 1 - he makes 10 damage
* Attack 2 - he makes 10 damage
* Attack 3 - he makes 10 damage
* Attack 4 - he makes 10 * 1.5 damage
* Attack 5 - he makes 10 damage
* ...
* Attack 8 - he makes 10 * 1.5 damage
* etc.

### Mechanics of a Boss Fight

If we kill a boss, the following things happen:

* Our maximum health is increased by 10%
* Our weapon damage is increased by 5%
* Our critical strike chance is increased by 3%
* The hero is healed to his new maximum health

## The Fight

Implement a ```Fight``` class, that simulates a fight between a Hero and an Enemy.
The enemy can be a Python or a Boss!

The class takes two arguments in the constructor:

* A ```Hero``` instance
* A ```Enemy``` instance

The ```Fight``` class flips a coin and decides which will attack first. (Imagine, take random between 0 and 100. If it is < 50, hero attacks first, else enemy attacks first)

Implement a ```simulate_fight()``` method, which starts a fight between the hero and the enemy, and prints out the status of the battle to the console.

The fight ends, when either the hero or the enemy dies!

__The method should return the winner of the Fight__
