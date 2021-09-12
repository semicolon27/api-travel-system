"""
Manajemen data tabel Currency
"""
from app.schema.http_schema import Response
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.dependency import get_db
from app.services.master import currency_service
from app.schema.master.currency_schema import Currency
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/master/currency", response_model=Response[List[Currency]], tags=["Currency"])
async def get_currencies(db: session = Depends(get_db)):
    res = Response
    res.data = currency_service.get_currencies(db)
    return res


@router.get("/master/currency/{currency_id}", response_model=Response[Currency], tags=["Currency"])
async def get_currency_by_id(currency_id, db: session = Depends(get_db)):
    res = Response
    res.data = currency_service.get_currency_by_id(db, currency_id)
    return res


@router.get("/master/currency/search/{keyword}", response_model=Response[List[Currency]], tags=["Currency"])
async def search_currency(keyword, db: session = Depends(get_db)):
    res = Response
    res.data = currency_service.search_currencies(db, keyword)
    return res


@router.post("/master/currency", response_model=Response[Currency], tags=["Currency"])
async def add_currency(currency: Currency, db: session = Depends(get_db)):
    res = Response
    res.data = currency_service.add_currency(db, currency)
    return res


@router.put("/master/currency", response_model=Response[Currency], tags=["Currency"])
async def edit_currency(currency: Currency, db: session = Depends(get_db)):
    res = Response
    res.data = currency_service.edit_currency(db, currency)
    return res


@router.delete("/master/currency", response_model=Response[Currency], tags=["Currency"])
async def delete_currency(currency: Currency, db: session = Depends(get_db)):
    res = Response
    res.data = currency_service.delete_currency(db, currency)
    return res
