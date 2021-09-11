from app.schema.http_schema import Response
from app.dependency import get_db
from typing import List
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.services.master import city_service
from fastapi import APIRouter
from app.schema.master.city_schema import City

router = APIRouter()


@router.get("/master/city", response_model=Response[List[City]], tags=["City"])
async def get_cities(db: session = Depends(get_db)):
    res = Response
    res.rc = '000'
    res.msg = 'Sukses'
    res.data = city_service.get_cities(db)
    return res


@router.get("/master/city/{city_id}", tags=["City"])
async def get_city_by_id(city_id, db: session = Depends(get_db)):
    categories = city_service.get_city_by_id(db, city_id)
    return categories


@router.post("/master/city", tags=["City"])
async def add_city(db: session = Depends(get_db)):
    return []


@router.put("/master/city", tags=["City"])
async def edit_city(db: session = Depends(get_db)):
    return []


@router.delete("/master/city", tags=["City"])
async def delete_city(db: session = Depends(get_db)):
    return []
