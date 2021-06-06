from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from app.services import product_service

router = APIRouter()

class Category(BaseModel):
    CategoryID: str
    CategoryDesc: str

@router.get("/product/category", response_model=List[Category], tags=["product", "category"])
async def get_product_category():
    categories = await product_service.get_categories()
    return categories
