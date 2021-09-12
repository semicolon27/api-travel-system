"""
Helo
"""
from app.schema.master.currency_schema import Currency
from app.models.db_models import T_Currency
from sqlalchemy.orm import Session
from sqlalchemy import desc


def get_currencies(db: Session):
    all_get = db.query(T_Currency).order_by(desc(T_Currency.Name)).all()
    return all_get


def search_currencies(db: Session, keyword: str):
    result = db.query(T_Currency).filter(
        T_Currency.Name.like(f"%{keyword}%")).all()
    print(result)
    return result


def get_currency_by_id(db: Session, currency_id):
    currency_by_id = db.query(T_Currency).filter(
        T_Currency.CurrencyID == currency_id).first()
    return currency_by_id


def add_currency(db: Session, currency: Currency):
    db_currency = T_Currency(**currency.dict())
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency


def edit_currency(db: Session, currency: Currency) -> Currency:
    edited_currency = get_currency_by_id(db, currency.CurrencyID)
    currency_new = T_Currency(**currency.dict())

    edited_currency.Name = currency_new.Name
    edited_currency.countryID = currency_new.countryID
    edited_currency.locKind = currency_new.locKind

    db.commit()
    db.refresh(edited_currency)

    return currency


def delete_currency(db: Session, currency: Currency):
    deleted_currency = get_currency_by_id(db, currency.CurrencyID)
    db.delete(deleted_currency)
    db.commit()
    return deleted_currency
