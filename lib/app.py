#Importing from sqlalchemy 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class Land_Owner initialized and the attributes declared
class Land_Owner(Base):
    __tablename__ = 'land_owners'

    owner_id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100))
    phone_number = Column(String(30))
    date_of_acquisition = Column(String(45))

    #one to many relationship
    manager_id = Column(Integer, ForeignKey('property_managers.manager_id'))
    manager = relationship('Property_Manager', back_populates = 'owner')

    # one to many relationship
    lands = relationship('Land', back_populates = 'owner')

# Property managers class and the attributes it constitutes of
class Property_Manager(Base):
    __tablename__ = 'property_managers'

    manager_id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100))
    gender = Column(String(10))
    contact = Column(String(20))

    estate_id = Column(Integer, ForeignKey('real_estate.estate_id'))
    estate = relationship('Real_Estate', back_populates = 'managers')
    owner = relationship('Land_Owner', back_populates = 'manager')
    lands_managers = relationship('LandsManager', back_populates = 'manager')

class Land(Base):
    __tablename__ = 'lands'

    land_id = Column(Integer, primary_key = True, autoincrement = True)
    place = Column(String(30))
    size = Column(String(20))

    owner_id = Column(Integer, ForeignKey('land_owners.owner_id'), unique = True)
    owner = relationship('Land_Owner', back_populates='lands')
    lands_managers = relationship('LandsManager', back_populates = 'land')


# class real estate initialized and the attributes declared
class Real_Estate(Base):
    __tablename__ = 'real_estate'

    estate_id = Column(Integer, primary_key = True, autoincrement = True)
    property_name = Column(String(50))

    managers = relationship('Property_Manager', back_populates = 'estate')


# Lands Manager table declared with its attributes
class LandsManager(Base):
    __tablename__ = 'lands_managers'

    lm_id = Column(Integer, primary_key = True, autoincrement = True)

    # many to many relationship
    land_id = Column(Integer, ForeignKey('lands.land_id'))
    manager_id = Column(Integer, ForeignKey('property_managers.manager_id'))

    land = relationship('Land', back_populates = 'lands_managers')
    manager = relationship('Property_Manager', back_populates = 'lands_managers')
