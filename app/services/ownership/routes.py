from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.ownership import ownership, schemas


router = APIRouter(prefix="/ownership", tags=["Ownership"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/{identifier}", response_model=schemas.CompanyOwnership)
def get_ownership(identifier: str, db: Session = Depends(get_db)):
    data = ownership.get_ownership_details(db, identifier)
    if not data:
        raise HTTPException(status_code=404, detail="Company not found")
    return data
