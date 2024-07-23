from fastapi import APIRouter, Form, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from datetime import date
from database import SessionLocal
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import IntegrityError
from sqlalchemy import distinct

baro = APIRouter()
templates = Jinja2Templates(directory="templates")

# 바로 등급 페이지
@baro.get("/baro")
async def read_join(request: Request):
    return templates.TemplateResponse("baro_service/baro.html", {"request": request})