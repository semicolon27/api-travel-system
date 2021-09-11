from app.schema.master.product_schema import Category
from app.dependency import get_db
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.services.master import product_service

router = APIRouter()


@router.get("/master/product/category", response_model=List[Category], tags=["Product"])
async def get_product_category(db: session = Depends(get_db)):
    categories = product_service.get_categories(db)
    return categories


@router.post("/master/product/category", response_model=Category)
async def create_item(item: Category, db: session = Depends(get_db)):
    return item
