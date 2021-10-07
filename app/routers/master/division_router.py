"""
Manajemen data tabel Division
DIVISON TIDAK MEMILIKI HALAMAN MASTER, JADI INI NANTI BUAT HALAMAN LAIN
"""
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import session
from app.schema.http_schema import Response
from app.dependency import get_db
from app.services.master import division_service
from app.schema.master.division_schema import Division, RequestDivisionByCode

router = APIRouter()


@router.post("/master/division/by-code", response_model=Response[Division], tags=["Division"])
async def get_division_by_code(data: RequestDivisionByCode, db: session = Depends(get_db)):
    res = Response
    res.data = division_service.get_division_by_code(db, data)
    return res
