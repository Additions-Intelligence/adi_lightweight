from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.firmographics import firmographics, schemas

router = APIRouter(prefix="/firmographics", tags=["Firmographics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{identifier}", response_model=schemas.CompanyOut)
def get_company_data(identifier: str, db: Session = Depends(get_db)):
    company = firmographics.get_company_with_relations(db, identifier)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
