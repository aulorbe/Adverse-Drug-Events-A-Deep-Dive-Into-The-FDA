from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, create_engine,or_
from sqlalchemy.orm import relationship
import sqlalchemy
from dash_package.__init__ import db
# Base = declarative_base()

class Adverse_Events(db.Model): #association table
    __tablename__ = 'events'
    id = Column(db.Integer, primary_key = True)
    sex = Column(db.Integer) #should we do int or text here?
    age = Column(db.Integer)

    brands = relationship('Brands', secondary = 'brands_events', back_populates='events')
    reactions = relationship('Reactions', secondary = 'reactions_events', back_populates='events')
    holidays = relationship('Holidays', back_populates='events',uselist=False)
    holiday_id = Column(db.Integer, ForeignKey('holidays.id'))


class Brands(db.Model): # many brand-drugs are associated with many manufacturers through adverse events
    __tablename__ = 'brands'
    id = Column(db.Integer, primary_key = True)
    name = Column(db.Text)
    events = relationship('Adverse_Events', secondary = 'brands_events',back_populates='brands') #many:many
    # many:many through association table

class Brands_Events(db.Model):
    __tablename__ = 'brands_events'
    brand_id = Column(db.Integer, ForeignKey('brands.id'), primary_key = True)
    event_id = Column(db.Integer, ForeignKey('events.id'), primary_key = True)



class Reactions(db.Model): #many reactions from 1 or more drugs through an adverse event
    __tablename__ = 'reactions'
    id = Column(db.Integer, primary_key = True)
    name = Column(db.Text)
    events = relationship('Adverse_Events', secondary='reactions_events', back_populates='reactions')


class Reactions_Events(db.Model):
    __tablename__ = 'reactions_events'
    reactions_id = Column(db.Integer, ForeignKey('reactions.id'), primary_key = True)
    event_id = Column(db.Integer, ForeignKey('events.id'), primary_key = True)



class Holidays(db.Model): # one holiday to many adverse events
    __tablename__ = 'holidays'
    id = Column(db.Integer, primary_key = True)
    name = Column(db.Text)
    date = Column(db.Text) #text? YYYY-MM-DD?
    events = relationship('Adverse_Events', back_populates='holidays')

# engine = sqlalchemy.create_engine('sqlite:///adverse-events.db', echo=True)
# Base.metadata.create_all(engine)
