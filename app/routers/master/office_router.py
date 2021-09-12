"""
Manajemen data tabel BranchOffice
"""
from app.schema.http_schema import Response
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.dependency import get_db
from app.services.master import office_service
from app.schema.master.office_schema import BranchOffice
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/master/office", response_model=Response[List[BranchOffice]], tags=["BranchOffice"])
async def get_offices(db: session = Depends(get_db)):
    res = Response
    res.data = office_service.get_offices(db)
    return res


@router.get("/master/office/{office_id}", response_model=Response[BranchOffice], tags=["BranchOffice"])
async def get_office_by_id(office_id, db: session = Depends(get_db)):
    res = Response
    res.data = office_service.get_office_by_id(db, office_id)
    return res


@router.get("/master/office/search/{keyword}", response_model=Response[List[BranchOffice]], tags=["BranchOffice"])
async def search_office(keyword, db: session = Depends(get_db)):
    res = Response
    res.data = office_service.search_offices(db, keyword)
    return res


@router.post("/master/office", response_model=Response[BranchOffice], tags=["BranchOffice"])
async def add_office(office: BranchOffice, db: session = Depends(get_db)):
    res = Response
    res.data = office_service.add_office(db, office)
    return res


@router.put("/master/office", response_model=Response[BranchOffice], tags=["BranchOffice"])
async def edit_office(office: BranchOffice, db: session = Depends(get_db)):
    res = Response
    res.data = office_service.edit_office(db, office)
    return res


@router.delete("/master/office", response_model=Response[BranchOffice], tags=["BranchOffice"])
async def delete_office(office: BranchOffice, db: session = Depends(get_db)):
    res = Response
    res.data = office_service.delete_office(db, office)
    return res
