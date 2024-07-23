
from database import SessionLocal
from sqlalchemy import distinct
from sqlalchemy.exc import IntegrityError
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from models.baro_models import CompanyInfo


def get_corp_info(corp_code: str):
    db: Session = SessionLocal()
    try:
        selectedcompany = db.query(CompanyInfo).filter(CompanyInfo.corp_code == corp_code).first()
        return selectedcompany
    finally:
        db.close()