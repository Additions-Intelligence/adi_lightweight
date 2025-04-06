from sqlalchemy.orm import Session, joinedload
from app.models import Company

def get_company_with_relations(db: Session, identifier: str):
    return db.query(Company).options(
        joinedload(Company.market_listings),
        joinedload(Company.employees),
        joinedload(Company.branches),
        joinedload(Company.auditors),
        joinedload(Company.solicitors),
        joinedload(Company.key_people),
        joinedload(Company.competitors),
    ).filter(
        (Company.ai_code == identifier) | (Company.isin == identifier)
    ).first()
