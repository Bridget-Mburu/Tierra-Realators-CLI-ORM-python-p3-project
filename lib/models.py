# importing of the required items to run the program
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base, Land_Owner, Property_Manager, Land, Real_Estate, LandsManager

# Connecting to the database
engine = create_engine('sqlite:///management.db')

# Ineracting with the database
Session = sessionmaker(bind=engine)


@click.group()
# entry line for CLI
def cli():
    pass 

# while loop to exit the loop
@cli.command()
def exit_program():
    click.echo("Exiting the program!!")
    raise click.Abort()

# method of adding land to the db and the argument required
@cli.command()
@click.option('--place', prompt = 'Enter the land place: ')
@click.option('--size', prompt = 'Enter the land size: ')
@click.option('--owner_id', prompt = 'Enter the Land Owner ID: ')
def add_land(place, size, owner_id):
    sesh = Session()
    new_land = Land(place=place, size=size, owner_id=owner_id)
    sesh.add(new_land)
    sesh.commit()
    sesh.close()
    click.echo(f"Added land: {place} {size}, Owner ID {owner_id}")

# method to liost all lands on the db
@cli.command()
def listing_lands():
    sesh = Session()
    lands = sesh.query(Land).all()

    land_list = [(land.land_id, land.place, land.size, land.owner_id) for land in lands]

    for land in land_list:
        click.echo(f"Land ID: {land[0]}, Place: {land[1]}, Size: {land[2]}, Owner ID: {land[3]}")

    sesh.close()

# to view details of a specific land by getting a land by id 
@cli.command()
@click.option('--land_id', prompt = 'Enter Land ID: ')
def show_land(land_id):
    sesh = Session()
    land = sesh.query(Land).filter(Land.land_id == land_id).first()
    sesh.close()

    if land:
        click.echo(f"Land ID: {land.land_id}, Place: {land.place}, Size: {land.size}")

    else:
        click.echo("Land not found")

# method to add a property manager in the database
@cli.command()
@click.option('--name', prompt = 'Enter Name: ')
@click.option('--gender', type= click.Choice(["Male", "Female"]), prompt = 'Enter Gender: ')
@click.option('--contact', prompt = 'Contact: ')
@click.option('--estate_id', prompt = 'Estate id: ')
def add_property_manager(name, gender, contact, estate_id):
    sesh = Session()
    new_manager = Property_Manager(name=name, gender=gender, contact=contact, estate_id=estate_id)
    sesh.add(new_manager)
    sesh.commit()
    sesh.close()
    click.echo(f"Property Manager {name} added successfully!!!!!!!!!")

# method to list the property manager in the db
@cli.command()
def listing_property_managers():
    sesh = Session()
    managers = sesh.query(Property_Manager).all()

    managers_list = [(manager.manager_id, manager.name, manager.gender, manager.contact, manager.estate_id) for manager in managers]

    for manager in managers_list:
        click.echo(f"ID: {manager[0]}, Name: {manager[1]}, Gender {manager[2]}, Contact: {manager[3]}, Estate id: {manager[4]}")

        sesh.close()

# method to delete a manager from the database else if id not found error raised
@cli.command()
@click.option('--manager_id', prompt = 'Manager ID')
def remove_manager(manager_id):
    sesh = Session()
    manager = sesh.query(Property_Manager).filter(Property_Manager.manager_id == manager_id).first()

    if manager:
        sesh.delete(manager)
        sesh.commit()
        click.echo(f"ID {manager_id} successfully deleted")

    else:
        click.echo(f"ID {manager_id} Manager not found")

        sesh.close()

#method to add the lands managers relationship
@cli.command()
@click.option('--land_id', prompt = 'Enter Land ID: ')
@click.option('--manager_id', prompt = 'Enter Manager ID: ')
def add_lands_manager(land_id, manager_id):
    sesh = Session()
    new_landsManager = LandsManager(land_id=land_id, manager_id=manager_id)
    sesh.add(new_landsManager)
    sesh.commit()
    sesh.close()
    click.echo(f"Land ID: {land_id} to Manager ID: {manager_id}")


# method to add land owner to the database 
@cli.command()
@click.option('--name', prompt = "Enter land owner's name")
@click.option('--phone_number', prompt = 'Enter Phone Number: ')
@click.option('--date_of_acquisition', prompt = 'Enter the Date of Acquisition')
@click.option('--manager_id', prompt = 'Enter Manager ID')
def add_land_owner(name, phone_number, date_of_acquisition, manager_id):
    sesh = Session()
    new_land_owner = Land_Owner(name=name, phone_number=phone_number, date_of_acquisition=date_of_acquisition, manager_id=manager_id)
    sesh.add(new_land_owner)
    sesh.commit()
    sesh.close()
    click.echo(f"Thank you {name} for purchsing land. Congratulations!!!!!")

# method to add areal estate to the program
@cli.command()
@click.option('--property_name', prompt = 'Enter Property Manager: ')
def add_real_estate(property_name):
    sesh = Session()
    new_real_estate = Real_Estate(property_name=property_name)
    sesh.add(new_real_estate)
    sesh.commit()
    sesh.close()
    click.echo(f"{property_name} added to the program")

# connects with the app.py
if __name__ == '__main__':
    while True:
        try:
            cli()
        except click.Abort:
            break