from app.schema.products_schema import Category
from app.dependency import get_db
from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.services import product_service

router = APIRouter()


@router.get("/product/category", response_model=List[Category], tags=["Product"])
async def get_product_category(db: session = Depends(get_db)):
    categories = product_service.get_categories(db)
    return categories
