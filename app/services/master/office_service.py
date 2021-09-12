"""
Helo
"""
from app.schema.master.office_schema import BranchOffice
from app.models.db_models import T_BranchOffice
from sqlalchemy.orm import Session
from sqlalchemy import desc


def get_offices(db: Session):
    all_get = db.query(T_BranchOffice).order_by(desc(T_BranchOffice.name)).all()
    return all_get


def search_offices(db: Session, keyword: str):
    result = db.query(T_BranchOffice).filter(
        T_BranchOffice.name.like(f"%{keyword}%")).all()
    print(result)
    return result


def get_office_by_id(db: Session, office_id):
    office_by_id = db.query(T_BranchOffice).filter(
        T_BranchOffice.OffCode == office_id).first()
    return office_by_id


def add_office(db: Session, office: BranchOffice):
    db_office = T_BranchOffice(**office.dict())
    db.add(db_office)
    db.commit()
    db.refresh(db_office)
    return db_office


def edit_office(db: Session, office: BranchOffice) -> BranchOffice:
    edited_office = get_office_by_id(db, office.OfficeID)
    office_new = T_BranchOffice(**office.dict())

    edited_office.Name = office_new.name
    edited_office.OfficeID = office_new.OffCode

    db.commit()
    db.refresh(edited_office)

    return office


def delete_office(db: Session, office: BranchOffice):
    deleted_office = get_office_by_id(db, office.OfficeID)
    db.delete(deleted_office)
    db.commit()
    return deleted_office
