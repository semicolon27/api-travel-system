from fastapi import FastAPI
from .models import db_models
from .routers.master import product_router, city_router
from .database import SessionLocal, engine

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True, title="Travel System API")
# app = FastAPI(debug=False, title="Travel System API", docs_url=None, redoc_url=None, openapi_url=None)

app.include_router(product_router.router)
app.include_router(city_router.router)

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=7700,
                reload=True,
                debug=True)
