"""
Manajemen data tabel City
"""
from app.schema.http_schema import Response
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.dependency import get_db
from app.services.master import city_service
from app.schema.master.city_schema import City
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/master/city", response_model=Response[List[City]], tags=["City"])
async def get_cities(db: session = Depends(get_db)):
    res = Response
    res.data = city_service.get_cities(db)
    return res


@router.get("/master/city/{city_id}", response_model=Response[City], tags=["City"])
async def get_city_by_id(city_id, db: session = Depends(get_db)):
    res = Response
    res.data = city_service.get_city_by_id(db, city_id)
    return res


@router.get("/master/city/search/{keyword}", response_model=Response[List[City]], tags=["City"])
async def search_city(keyword, db: session = Depends(get_db)):
    res = Response
    res.data = city_service.search_cities(db, keyword)
    return res


@router.post("/master/city", response_model=Response[City], tags=["City"])
async def add_city(city: City, db: session = Depends(get_db)):
    res = Response
    res.data = city_service.add_city(db, city)
    return res


@router.put("/master/city", response_model=Response[City], tags=["City"])
async def edit_city(city: City, db: session = Depends(get_db)):
    res = Response
    res.data = city_service.edit_city(db, city)
    return res


@router.delete("/master/city", response_model=Response[City], tags=["City"])
async def delete_city(city: City, db: session = Depends(get_db)):
    res = Response
    res.data = city_service.delete_city(db, city)
    return res
