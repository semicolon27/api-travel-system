from typing import List
from fastapi import Depends, FastAPI
import databases
import sqlalchemy
from .models import db_models
from .dependencies import get_query_token, get_token_header
from .routers import items, users, product_router
from app.utils.database import database as db, DATABASE_URL

app = FastAPI()

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

db_models.metadata.create_all(engine)

@app.on_event("startup")
async def connect():
    print("Create Connection to Database")
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    print("Disconnect From Database")
    await db.disconnect()

@app.get('/babi', response_model=List[product_router.Category])
async def hello():
    hei = await db.fetch_all("SELECT * FROM Category")
    print("hei")
    print(hei)
    return "SUkses"

@app.get('/tambah', response_model=List[product_router.Category])
async def hello():
    hei = await db.execute("INSERT INTO Category VALUES ('03', 'Hadiah')")
    return hei

app.include_router(product_router.router)