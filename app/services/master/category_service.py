"""
Helo
"""
from app.schema.master.category_schema import Category
from app.models.db_models import T_Category
from sqlalchemy.orm import Session
from sqlalchemy import desc


def get_categories(db: Session):
    all_get = db.query(T_Category).order_by(desc(T_Category.CategoryDesc)).all()
    return all_get


def search_categories(db: Session, keyword: str):
    result = db.query(T_Category).filter(
        T_Category.CategoryDesc.like(f"%{keyword}%")).all()
    print(result)
    return result


def get_category_by_id(db: Session, category_id):
    category_by_id = db.query(T_Category).filter(
        T_Category.CategoryID == category_id).first()
    return category_by_id


def add_category(db: Session, category: Category):
    db_category = T_Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def edit_category(db: Session, category: Category) -> Category:
    edited_category = get_category_by_id(db, category.CategoryID)
    category_new = T_Category(**category.dict())

    edited_category.CategoryDesc = category_new.CategoryDesc

    db.commit()
    db.refresh(edited_category)

    return category


def delete_category(db: Session, category: Category):
    deleted_category = get_category_by_id(db, category.CategoryID)
    db.delete(deleted_category)
    db.commit()
    return deleted_category
