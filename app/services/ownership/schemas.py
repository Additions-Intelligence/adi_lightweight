from typing import List, Optional
from pydantic import BaseModel


class BeneficialOwner(BaseModel):
    id: int
    name: str
    amount: Optional[float] = None
    percentage: Optional[float] = None
    country: Optional[str] = None
    type: Optional[str] = None

    class Config:
        from_attributes = True


class OwnershipDetail(BaseModel):
    id: int
    company_id: int 
    year: int
    total_shares: Optional[int] = None
    total_percentage: Optional[float] = None
    beneficial_owners: List[BeneficialOwner] = []

    class Config:
        from_attributes = True


class CompanyOwnership(BaseModel):
    id: int
    name: str
    isin: str
    ai_code: str
    ownerships: List[OwnershipDetail] = []  # List of ownership details

    class Config:
        from_attributes = True
