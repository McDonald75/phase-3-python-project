from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Trainer(Base):
    __tablename__ = 'trainers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialization = Column(String)
    members = relationship('Member', back_populates='trainer')

    def __repr__(self):
        return f"Trainer(id={self.id}, name='{self.name}', specialization='{self.specialization}')"

class Fitnessplan(Base):
    __tablename__ = 'fitnessplans'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    duration_weeks = Column(Integer)
    members = relationship('Member', back_populates='fitnessplan')

    def __repr__(self):
        return f"Fitnessplan(id={self.id}, name='{self.name}', duration_weeks={self.duration_weeks})"

class Member(Base):
    __tablename__ = 'members'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    trainer_id = Column(Integer, ForeignKey('trainers.id'))
    fitnessplan_id = Column(Integer, ForeignKey('fitnessplans.id'))
    
    trainer = relationship('Trainer', back_populates='members')
    fitnessplan = relationship('Fitnessplan', back_populates='members')

    def __repr__(self):
        return f"Member(id={self.id}, name='{self.name}', email='{self.email}')"

engine = create_engine('sqlite:///jim_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()