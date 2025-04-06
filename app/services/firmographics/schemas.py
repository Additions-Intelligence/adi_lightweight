from typing import List, Optional
from pydantic import BaseModel
#from datetime import date

class MarketListing(BaseModel):
    country: str
    date_listed: Optional[str]
    symbol: Optional[str]
    stock_exchange: Optional[str]

    class Config:
        from_attributes = True

class EmployeeCount(BaseModel):
    year: int
    count: int

    class Config:
        from_attributes = True

class BranchCount(BaseModel):
    year: int
    count: int

    class Config:
        from_attributes = True

class Auditor(BaseModel):
    year: int
    auditor_name: str

    class Config:
        from_attributes = True

class Solicitor(BaseModel):
    year: int
    solicitor_name: str

    class Config:
        from_attributes = True

class KeyPerson(BaseModel):
    name: str
    title: Optional[str]
    profession: Optional[str]
    age: Optional[int]
    nationality: Optional[str]
    education: Optional[str]

    class Config:
        from_attributes = True

class Competitor(BaseModel):
    competitor_name: str

    class Config:
        from_attributes = True

class CompanyOut(BaseModel):
    ai_code: Optional[str]
    isin: Optional[str]
    name: str
    sector: Optional[str]
    country: Optional[str]
    listed: Optional[str]
    market_listings: List[MarketListing] = []
    employees: List[EmployeeCount] = []
    branches: List[BranchCount] = []
    auditors: List[Auditor] = []
    solicitors: List[Solicitor] = []
    key_people: List[KeyPerson] = []
    competitors: List[Competitor] = []

    class Config:
        from_attributes = True
