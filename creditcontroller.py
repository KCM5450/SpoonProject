from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from credit_review_create import summarize_report
from dependencies import get_db
import requests
import pandas as pd
import os
from dotenv import load_dotenv

creditreview = APIRouter()
template1 = Jinja2Templates(directory="templates/creditreview")

# .env 파일에서 환경 변수를 로드합니다
load_dotenv()


@creditreview.get("/createReview/")
async def create_review(db: Session = Depends(get_db)):
    # finanical_summary_v1의 회사코드 리스트 가져오기
    corp_code = "00164779"  # 에스케이하이닉스(주)
    # 받아온 회사 코드로 최신 정기 공시보고서 번호 dart api로부터 받아오기
    summary = summarize_report(corp_code)
    return {"result": "DB success"}


@creditreview.get("/creditReview/")
async def read_credit(request: Request, db: Session = Depends(get_db)):
    # 업체 list 뽑아서 넘기기
    return template1.TemplateResponse("review_search.html", {"request": request})


# @creditreview.get("/creditReview/detail/{corp_code}")
# async def reviewDetail(request: Request, corp_code: int, db: Session = Depends(get_db)):

#     return summary
