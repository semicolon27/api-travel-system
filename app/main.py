from fastapi import FastAPI
from .models import db_models
from .routers.master import product_router, city_router
from .database import SessionLocal, engine

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_router.router)
app.include_router(city_router.router)
