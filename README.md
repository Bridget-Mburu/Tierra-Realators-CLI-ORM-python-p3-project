# Tierra Realators

## Description
The program enables real estate companies to track the work done by each property manager and gives people a chance to purchase land from them. This reduces the chances of corruption that may take place since everyone involved is exposed on the program.

## Installation
To set up the program follow the following steps one by one:

### Prerequisites
- Python 3.8.10
- Git (for cloning the repository)

### Steps
1. Clone the repository

2. Install virtual environment
    `pipenv install`

3. Installing the dependencies which are the SQLAlchemy and Alembic
    `pip install sqlalchemy alembic`

4. Run `pipenv shell` to enter the virtual environment

5. To install alembic folder and files
        `alembic init migrations`

6. To install click 
        `pip install click`

7. To exit the virtual environment run 
        `exit`

## Features
A database named management.db is created where all the data in the tables are updated.

The tables created and modified by python ORM method are as follows:
- `Land_Owner`
- `Property_Manager`
- `Land`
- `Real_Estate`
- `LandsManager`

### Relationship
###### Land_Owners table
- Has a one to one relationship with the `Property_Manager` table.
- Has a one to many relationship with the `Land` table where an owner can purchase many lands as possible.

###### Property_Manager table
- Has a one to many relationship with the `Real_Estate` for a company can have a lot of managers.

###### LandsManager table
- Has a many to many relationship between the `Lands` table and `Property_Manager` table


### CLI
click function is used to enable one to interact with the program

- To display the menu run:
    `python3 models.py`

###### The following are displayed in the menu and this are the command lines to execute to interact with the database
`add-land`
- python3 models.py add-land <"place"> <"size acres"> <owner_id>

`add-land-owner`
- python3 models.py add-land-owner <"name"> <"phone_number"> <"date_of_acquisition">

`add-property`
- python3 models.py add-property <"name"> <"gender"> <"contact"> <estate_id>

`add-real-estate`
- python3 models.py add-real-estate <"property_name">

`listing-lands`
- python3 models.py listing-lands

`listing-property-managers`
- python3 models.py listing-property-managers

`remove-manager`
- python3 models.py remove-manager
- A promp of ID pops up -- Enter the id of the manager you would like to remove from the program

`show-land`
- python3 models.py show-land <land_id>

## Author
Bridget Mburu - Initial work

## Schema 
- dbdiagram - `https://dbdiagram.io/d/Tierra-Realators-66e88f1e6dde7f4149494513`

## Demo 


## Resources
`https://click.palletsprojects.com/en/8.1.x/`







