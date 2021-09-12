"""
Manajemen data tabel Category
"""
from app.schema.http_schema import Response
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.dependency import get_db
from app.services.master import category_service
from app.schema.master.category_schema import Category
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/master/category", response_model=Response[List[Category]], tags=["Category"])
async def get_categories(db: session = Depends(get_db)):
    res = Response
    res.data = category_service.get_categories(db)
    return res


@router.get("/master/category/{category_id}", response_model=Response[Category], tags=["Category"])
async def get_category_by_id(category_id, db: session = Depends(get_db)):
    res = Response
    res.data = category_service.get_category_by_id(db, category_id)
    return res


@router.get("/master/category/search/{keyword}", response_model=Response[List[Category]], tags=["Category"])
async def search_category(keyword, db: session = Depends(get_db)):
    res = Response
    res.data = category_service.search_categories(db, keyword)
    return res


@router.post("/master/category", response_model=Response[Category], tags=["Category"])
async def add_category(category: Category, db: session = Depends(get_db)):
    res = Response
    res.data = category_service.add_category(db, category)
    return res


@router.put("/master/category", response_model=Response[Category], tags=["Category"])
async def edit_category(category: Category, db: session = Depends(get_db)):
    res = Response
    res.data = category_service.edit_category(db, category)
    return res


@router.delete("/master/category", response_model=Response[Category], tags=["Category"])
async def delete_category(category: Category, db: session = Depends(get_db)):
    res = Response
    res.data = category_service.delete_category(db, category)
    return res
