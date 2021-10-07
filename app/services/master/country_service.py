"""
Helo
"""
from app.schema.master.country_schema import Country
from app.models.db_models import T_Country
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List


def get_countries(db: Session):
    all_get = db.query(T_Country).order_by(desc(T_Country.Name)).all()
    return all_get


def search_countries(db: Session, keyword: str):
    result = db.query(T_Country).filter(
        T_Country.Name.like(f"%{keyword}%")).all()
    print(result)
    return result


def get_country_by_id(db: Session, country_id):
    country_by_id = db.query(T_Country).filter(
        T_Country.CountryID == country_id).first()
    return country_by_id


def add_country(db: Session, country: Country):
    db_country = T_Country(**country.dict())
    db.add(db_country)
    db.commit()
    return db_country

def add_countries(db: Session, country_list: List[Country]):
    try:
        for country in country_list:
            db_country = T_Country(**country.dict())
            db.add(db_country)
        db.commit()
    except Exception as e:
        db.rollback()
    return country_list


def edit_country(db: Session, country: Country) -> Country:
    edited_country = get_country_by_id(db, country.CountryID)
    country_new = T_Country(**country.dict())

    edited_country.Name = country_new.Name
    edited_country.CountryID = country_new.CountryID

    db.commit()
    db.refresh(edited_country)

    return country


def delete_country(db: Session, country_id: str):
    deleted_country = get_country_by_id(db, country_id)
    db.delete(deleted_country)
    db.commit()
    return deleted_country
