from fastapi import Depends, FastAPI
from .models import db_models
from .dependencies import get_query_token, get_token_header
from .routers import product_router
from .database import SessionLocal, engine

db_models.metadata.create_all(engine)

app = FastAPI()

app.include_router(product_router.router)
