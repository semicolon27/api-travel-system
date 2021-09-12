"""
Helo
"""
from app.schema.master.city_schema import City
from app.models.db_models import T_City
from sqlalchemy.orm import Session
from sqlalchemy import desc


def get_cities(db: Session):
    all_get = db.query(T_City).order_by(desc(T_City.Name)).all()
    return all_get


def search_cities(db: Session, keyword: str):
    result = db.query(T_City).filter(T_City.Name.like(f"%{keyword}%")).all()
    print(result)
    return result


def get_city_by_id(db: Session, city_id):
    city_by_id = db.query(T_City).filter(T_City.CityID == city_id).first()
    return city_by_id


def add_city(db: Session, city: City):
    db_city = T_City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def edit_city(db: Session, city: City) -> City:
    edited_city = get_city_by_id(db, city.CityID)
    city_new = T_City(**city.dict())

    edited_city.Name = city_new.Name
    edited_city.countryID = city_new.countryID
    edited_city.locKind = city_new.locKind

    db.commit()
    db.refresh(edited_city)

    return city


def delete_city(db: Session, city: City):
    deleted_city = get_city_by_id(db, city.CityID)
    db.delete(deleted_city)
    db.commit()
    return deleted_city
