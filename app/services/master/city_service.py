from app.models.db_models import T_City
from sqlalchemy.orm import Session
from sqlalchemy import desc


def get_cities(db: Session):
    # db.query ngga bisa pkai await
    all_get = db.query(T_City).order_by(desc(T_City.Name)).all()
    return all_get


def get_city_by_id(db: Session, city_id):
    # db.query ngga bisa pkai await
    all_get = db.query(T_City).filter(T_City.CityID == city_id)
    return all_get
