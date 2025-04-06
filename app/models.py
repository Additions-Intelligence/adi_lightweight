from app.database import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

#_______Firmographics_Start________
class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, autoincrement=False)
    ai_code = Column(String, unique=True, nullable=False)
    isin = Column(String, unique=True, nullable=True)
    company_reg_num = Column(String, unique=False, nullable=True)
    date_of_incorporation = Column(Integer, nullable=True)
    incorporation_note = Column(String, nullable=True)
    name = Column(String, nullable=False)
    holding_company = Column(String, nullable=True)
    corporate_action = Column(String, nullable=True)
    status = Column(String, nullable=True)
    description = Column(String, nullable=True)
    listed = Column(String, nullable=False)
    continent = Column(String, nullable=True)
    sub_continent = Column(String, nullable=True)
    country = Column(String, nullable=True)
    region = Column(String, nullable=True)
    head_office_location = Column(String, nullable=True)
    gps_coordinates = Column(String, nullable=True)
    postal_address = Column(String, nullable=True)
    digital_address = Column(String, nullable=True)
    telephone = Column(String, nullable=True)
    fax = Column(String, nullable=True)
    website = Column(String, nullable=True)
    contact_email = Column(String, nullable=True)
    sector = Column(String, nullable=True)
    subsector_activities = Column(String, nullable=True)
    nace_sector = Column(String, nullable=True)
    operational_classification = Column(String, nullable=True)
    state_owned = Column(String, nullable=True)
    keyword = Column(String, nullable=True)
    
    market_listings = relationship("MarketListing", back_populates="company")
    employees = relationship("EmployeeCount", back_populates="company")
    branches = relationship("BranchCount", back_populates="company")
    auditors = relationship("Auditor", back_populates="company")
    solicitors = relationship("Solicitor", back_populates="company")
    key_people = relationship("KeyPerson", back_populates="company")
    competitors = relationship("Competitor", back_populates="company")
    ownerships = relationship("OwnershipDetail", back_populates="company")

class MarketListing(Base):
    __tablename__ = 'market_listings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    country = Column(String, nullable=False)
    date_listed = Column(String, nullable=True)
    symbol = Column(String, nullable=True)
    stock_exchange = Column(String, nullable=True)
    company = relationship("Company", back_populates="market_listings")

class EmployeeCount(Base):
    __tablename__ = 'employee_counts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    year = Column(Integer, nullable=False)
    count = Column(Integer, nullable=True)
    company = relationship("Company", back_populates="employees")

class BranchCount(Base):
    __tablename__ = 'branch_counts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    year = Column(Integer, nullable=False)
    count = Column(Integer, nullable=True)
    company = relationship("Company", back_populates="branches")

class Auditor(Base):
    __tablename__ = 'auditors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    year = Column(Integer, nullable=False)
    auditor_name = Column(String, nullable=False)
    company = relationship("Company", back_populates="auditors")

class Solicitor(Base):
    __tablename__ = 'solicitors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    year = Column(Integer, nullable=False)
    solicitor_name = Column(String, nullable=False)
    company = relationship("Company", back_populates="solicitors")

class KeyPerson(Base):
    __tablename__ = 'key_people'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    name = Column(String, nullable=False)
    title = Column(String, nullable=True)
    profession = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    nationality = Column(String, nullable=True)
    education = Column(String, nullable=True)
    company = relationship("Company", back_populates="key_people")

class Competitor(Base):
    __tablename__ = 'competitors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    competitor_name = Column(String, nullable=False)
    company = relationship("Company", back_populates="competitors")

#_______Firmographics_End________


#_______Ownership_Start________
class OwnershipDetail(Base):
    __tablename__ = 'ownership_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    year = Column(Integer, nullable=False)
    total_shares = Column(Integer, nullable=True)
    total_percentage = Column(Float, nullable=True)
    company = relationship("Company", back_populates="ownerships")
    beneficial_owners = relationship("BeneficialOwner", back_populates="ownership_detail")

class BeneficialOwner(Base):
    __tablename__ = 'beneficial_owners'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ownership_detail_id = Column(Integer, ForeignKey('ownership_details.id'))
    name = Column(String, nullable=True)
    amount = Column(Float, nullable=True)
    percentage = Column(Float, nullable=True)
    country = Column(String, nullable=True)
    type = Column(String, nullable=True)
    ownership_detail = relationship("OwnershipDetail", back_populates="beneficial_owners")


#_______Ownership_End________