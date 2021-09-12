"""
Manajemen data tabel JobKind
"""
from app.schema.http_schema import Response
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.dependency import get_db
from app.services.master import jobkind_service
from app.schema.master.jobkind_schema import JobKind
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/master/jobkind", response_model=Response[List[JobKind]], tags=["JobKind"])
async def get_jobkinds(db: session = Depends(get_db)):
    res = Response
    res.data = jobkind_service.get_jobkinds(db)
    return res


@router.get("/master/jobkind/{jobkind_id}", response_model=Response[JobKind], tags=["JobKind"])
async def get_jobkind_by_id(jobkind_id, db: session = Depends(get_db)):
    res = Response
    res.data = jobkind_service.get_jobkind_by_id(db, jobkind_id)
    return res


@router.get("/master/jobkind/search/{keyword}", response_model=Response[List[JobKind]], tags=["JobKind"])
async def search_jobkind(keyword, db: session = Depends(get_db)):
    res = Response
    res.data = jobkind_service.search_jobkinds(db, keyword)
    return res


@router.post("/master/jobkind", response_model=Response[JobKind], tags=["JobKind"])
async def add_jobkind(jobkind: JobKind, db: session = Depends(get_db)):
    res = Response
    res.data = jobkind_service.add_jobkind(db, jobkind)
    return res


@router.put("/master/jobkind", response_model=Response[JobKind], tags=["JobKind"])
async def edit_jobkind(jobkind: JobKind, db: session = Depends(get_db)):
    res = Response
    res.data = jobkind_service.edit_jobkind(db, jobkind)
    return res


@router.delete("/master/jobkind", response_model=Response[JobKind], tags=["JobKind"])
async def delete_jobkind(jobkind: JobKind, db: session = Depends(get_db)):
    res = Response
    res.data = jobkind_service.delete_jobkind(db, jobkind)
    return res
