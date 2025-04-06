from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.services.firmographics import routes as firmographics_routes


app = FastAPI(title="Additional Intelligence App")

# Creating tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(firmographics_routes.router)
