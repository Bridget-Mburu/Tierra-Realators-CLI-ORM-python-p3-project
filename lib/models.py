import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base, Land_Owner, Property_Manager, Land, Real_Estate, LandsManager

engine = create_engine('sqlite:///management.db')
Session = sessionmaker(bind=engine)

@click.group()
# entry line for CLI
def cli():
    pass 

@cli.command()
@click.argument('place')
@click.argument('size')
@click.argument('owner_id')
def add_land(place, size, owner_id):
    sesh = Session()
    new_land = Land(place=place, size=size, owner_id=owner_id)
    sesh.add(new_land)
    sesh.commit()
    sesh.close()
    click.echo(f"Added land: {place} {size}, Owner ID {owner_id}")

@cli.command()
def listing_lands():
    sesh = Session()
    lands = sesh.query(Land).all()

    land_list = [(land.land_id, land.place, land.size, land.owner_id) for land in lands]

    for land in land_list:
        click.echo(f"Land ID: {land[0]}, Place: {land[1]}, Size: {land[2]}, Owner ID: {land[3]}")

        sesh.close()

@cli.command()
@click.argument('land_id')
def show_land(land_id):
    sesh = Session()
    land = sesh.query(Land).filter(Land.land_id == land_id).first()
    sesh.close()

    if land:
        click.echo(f"Land ID: {land.land_id}, Place: {land.place}, Size: {land.size}")

    else:
        click.echo("Land not found")

@cli.command()
@click.argument('name')
@click.argument('gender')
@click.argument('contact')
@click.argument('estate_id')
def add_property_manager(name, gender, contact, estate_id):
    sesh = Session()
    new_manager = Property_Manager(name=name, gender=gender, contact=contact, estate_id=estate_id)
    sesh.add(new_manager)
    sesh.commit()
    sesh.close()
    click.echo(f"Property Manager {name} added successfully!!!!!!!!!")

@cli.command()
def listing_property_managers():
    sesh = Session()
    managers = sesh.query(Property_Manager).all()

    managers_list = [(manager.manager_id, manager.name, manager.gender, manager.contact, manager.estate_id) for manager in managers]

    for manager in managers_list:
        click.echo(f"ID: {manager[0]}, Name: {manager[1]}, Gender {manager[2]}, Contact: {manager[3]}, Estate id: {manager[4]}")

        sesh.close()

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
        click.echo(f"ID {manager_id} Managaer not found")

        sesh.close()


@cli.command()
@click.argument('name')
@click.argument('phone_number')
@click.argument('date_of_acquisition')
@click.argument('manager_id')
def add_land_owner(name, phone_number, date_of_acquisition, manager_id):
    sesh = Session()
    new_land_owner = Land_Owner(name=name, phone_number=phone_number, date_of_acquisition=date_of_acquisition, manager_id=manager_id)
    sesh.add(new_land_owner)
    sesh.commit()
    sesh.close()
    click.echo(f"Thank you {name} for purchsing land. Congratulations!!!!!")

@cli.command()
@click.argument('property_name')
def add_real_estate(property_name):
    sesh = Session()
    new_real_estate = Real_Estate(property_name=property_name)
    sesh.add(new_real_estate)
    sesh.commit()
    sesh.close()
    click.echo(f"{property_name} added to the program")

if __name__ == '__main__':
    cli()