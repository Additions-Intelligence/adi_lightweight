from sqlalchemy.orm import Session, joinedload
from app.models import Company, OwnershipDetail


def get_ownership_details(db: Session, identifier: str):
    return db.query(Company).options(
        joinedload(Company.ownerships).joinedload(OwnershipDetail.beneficial_owners)
    ).filter(
        (Company.ai_code == identifier) | (Company.isin == identifier)
    ).first()
