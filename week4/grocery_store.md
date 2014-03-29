## Problem X.1 - Grocery store

With the knowledge gained by completing the previous exercises, you must create a grocery store,
using OOP, TDD and SQL.
The store will have a sqlite database storing all products that are available for sale.

### Creating the database structure
Create a script called ```create_store.py``` that creates the following table structure:

| id | name  | price_per_kg  | quantity_in_kg |
| ---|:-----:| ------ | -------- |



### Importing data
The data will be imported from a json file into the database.

```json
[
    {
        "name": "Potatoes",
        "price_per_kg": 1.2,
        "quantity_in_kg": 20
    },
    {
        "name": "Carrots",
        "price_per_kg": 1.1,
        "quantity_in_kg": 6
    },
    {
        "name": "Cucumbers",
        "price_per_kg": 2.2,
        "quantity_in_kg": 3
    },
    {
        "name": "Lettuce",
        "price_per_kg": 2.1,
        "quantity_in_kg": 7
    },
    {
        "name": "Tomatoes",
        "price_per_kg": 2.7,
        "quantity_in_kg": 10
    }
]
```

The now populated database

| id | name  | price_per_kg  | quantity_in_kg |
| ---|:-----:| ------ | -------- |
1| Potatoes | 1.20 | 20 |
2| Carrots | 1.1 | 6 |
3| Cucumbers | 2.20 | 3 |
4| Lettuce | 2.10 | 7 |
5| Tomatoes| 2.70 | 10 |


### Creating a parser
After we created a database and added our products for sale in it,
we would want to have a script that takes the following commands:
Create a script called ```manage_store.py``` that takes the following commands:

__Commands:__
* ```import_json <json_filename>``` - Adds products from the json file to the database.
* ```list_products``` - Prints out all products in the following format: "[id] name - price_per_kg BGN - quantity kg"
* ```add_product``` - Prompts for data, needed to add a new product to the database.
* ```delete_product <product_id>``` - Removes the product matching the product id in the database.
* ```update_product <product_id>``` - Updates the product data matching the product id in the database.
* ```export_json <json_filename>``` - Exports the database to a json file.

__Example usage of commands:__
```
command>import_json spring_sale_products.json
Imported spring_sale_products
```

```
command>list_products
[1] Potatoes - 1.20 BGN - 20 kg
[2] Carrots - 1.1 BGN - 6 kg
[3] Cucumbers - 2.2 BGN - 3 kg
[4] Lettuce - 2.1 BGN - 7 kg
[5] Tomatoes - 2.7 BGN - 10 kg
```

```
command>add_product
product name>Apples
price per kg>2
quantity>2
Added Apples to products.
```

```
command>delete_product 5
Tomatoes removed.
```

```
command>update_product 2
product name>Carrots
price per kg>1.8
quantity>5
```

```
command>export_json 123.json
Products were exported to 123.json
```

And this is exactly how the 123.json file looks:

```json
[
    {
        "name": "Potatoes",
        "price_per_kg": 1.2,
        "quantity_in_kg": 20
    },
    {
        "name": "Carrots",
        "price_per_kg": 1.8,
        "quantity_in_kg": 5
    },
    {
        "name": "Cucumbers",
        "price_per_kg": 2.2,
        "quantity_in_kg": 3
    },
    {
        "name": "Lettuce",
        "price_per_kg": 2.1,
        "quantity_in_kg": 7
    },
    {
        "name": "Apples",
        "price_per_kg": 2,
        "quantity_in_kg": 2
    }
]
```

## Problem X.2 - Grocery store customers
Now that we have a good base, let's extend it with customers.


### Adding a new table
Modify the ``create_database.py`` script and have it add another table for customers.
The customers table should have the following structure:

| id | name  | kg_bought  | money_spent |
| ---|:-----:| ------ | -------- |


### Import customers data
Again, the data will be imported from a json. File name is spring_customers.json

```json
[
    {
        "name": "Ivo",
        "kg_bought": 5.1,
        "money_spent": 17.7
    },
    {
        "name": "Rado",
        "price_per_kg": 3.2,
        "quantity_in_kg": 12.2
    }
]
```


The populated database with customers:

| id | name  | kg_bought  | money_spent |
| ---|:-----:| ------ | -------- |
1| Ivo | 5.1 | 17.7 |
2| Rado | 3.2 | 12.2 |


### Extending the parser
We want to have some more commands that will make use of the new table.
Most of them can be done with a little refactoring of the previous commands.


__A little commands refactoring:__
* ``import_json`` to ``import_products_json``
* ``export_json`` to ``export_products_json``

And make sure you change it at all places, so it doesn't break your program! :smile:

__Add these new commands:__
* ```import_json_customers <json_filename>``` - Adds customers from the json file to the database.
* ```list_customers``` - Prints out all customers in the following format: "[id] name - kg_bought kg - money_spent BGN"
* ```add_customer``` - Prompts for data, needed to add a new customer to the database.
* ```delete_customer <customer_id>``` - Removes the customer matching the customer id in the database.
* ```update_customer <customer_id>``` - Updates the customer data matching the customer id in the database.
* ```export_customers_json <json_filename>``` - Exports the customers in the database to a json file.


There's no need for example usage of commands since the commands are identical to the products commands.

However here's how the exported json customers file will look:

```
command>add_customer
name>Mityo
kg bought>10
money spent>21
Added Mityo to customers.
command>export_customers_json summer_customers.json
Customers were exported to summer_customers.json
```

And this is exactly how the summer_customers.json file looks:

```json
[
    {
        "name": "Ivo",
        "kg_bought": 5.1,
        "money_spent": 17.7
    },
    {
        "name": "Rado",
        "kg_bought": 3.2,
        "money_spent": 12.2
    }
    {
        "name": "Mityo",
        "kg_bought": 10,
        "money_spent": 21
    }
]
```

## Bonus round: Sales
After we passed all the obstacles, it's finally time to have sales.

__Commands:__
* ```buy <customer_id>``` - The given customer buys products available in the products table.

__Example usage:__

```
command>buy 1
~~~Ivo buys~~~
products - amount_in_kg>Apples - 2, Lettuce - 3.1
~~~Bill: 10.51~~~
command>list_products
....
[4] Lettuce - 2.1 BGN - 3.9 kg
[5] Apples - 2 BGN - 0 kg
command>list_customers
[1] Ivo - 10.2 kg - 28.21 BGN
...
```

```
command>buy 2
~~~Rado buys~~~
products - amount_in_kg>Apples - 2,
!Error: Apples out of stock.
```

```
command>buy 2
~~~Rado buys~~~
products - amount_in_kg>Ambrosia - 5,
!Error: Ambrosia not found in products.
```

## (Not yet added) Bonus round 2: Extend customers
Customers will now have a budget and can't godmode anymore.
Buying products over their budget will fail and successful buys will reduce their budget.
