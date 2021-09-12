"""
Manajemen data tabel Country
"""
from app.schema.http_schema import Response
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.dependency import get_db
from app.services.master import country_service
from app.schema.master.country_schema import Country
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/master/country", response_model=Response[List[Country]], tags=["Country"])
async def get_countries(db: session = Depends(get_db)):
    res = Response
    res.data = country_service.get_countries(db)
    return res


@router.get("/master/country/{country_id}", response_model=Response[Country], tags=["Country"])
async def get_country_by_id(country_id, db: session = Depends(get_db)):
    res = Response
    res.data = country_service.get_country_by_id(db, country_id)
    return res


@router.get("/master/country/search/{keyword}", response_model=Response[List[Country]], tags=["Country"])
async def search_country(keyword, db: session = Depends(get_db)):
    res = Response
    res.data = country_service.search_countries(db, keyword)
    return res


@router.post("/master/country", response_model=Response[Country], tags=["Country"])
async def add_country(country: Country, db: session = Depends(get_db)):
    res = Response
    res.data = country_service.add_country(db, country)
    return res


@router.put("/master/country", response_model=Response[Country], tags=["Country"])
async def edit_country(country: Country, db: session = Depends(get_db)):
    res = Response
    res.data = country_service.edit_country(db, country)
    return res


@router.delete("/master/country", response_model=Response[Country], tags=["Country"])
async def delete_country(country: Country, db: session = Depends(get_db)):
    res = Response
    res.data = country_service.delete_country(db, country)
    return res
