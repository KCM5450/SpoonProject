from fastapi import APIRouter, Form, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from datetime import date
from database import SessionLocal
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import IntegrityError
from sqlalchemy import distinct
from services_def.baro_service import get_corp_info



baro = APIRouter()
templates = Jinja2Templates(directory="templates")

# 바로 등급 검색 페이지
@baro.get("/baro")
async def read_join(request: Request):
    return templates.TemplateResponse("baro_service/baro_search.html", {"request": request})


@baro.get("/baro_info/{corp_code}")
async def search_corp(corp_code: str, request: Request):
    selectedcompany = get_corp_info(corp_code)
    print(type(selectedcompany))
    print(selectedcompany.corp_code)
    if selectedcompany:
        return JSONResponse (content={
            "corp_code": selectedcompany.corp_code
        })
