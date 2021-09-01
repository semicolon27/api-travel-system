import uvicorn
from fastapi import Depends, FastAPI
from app.models import db_models
from app.dependencies import get_query_token, get_token_header
from app.routers import product_router
from app.database import SessionLocal, engine

db_models.metadata.create_all(engine)

app = FastAPI(debug=True, title="Travel System API")
# app = FastAPI(debug=False, title="Travel System API", docs_url=None, redoc_url=None, openapi_url=None)

app.include_router(product_router.router)

if __name__ == '__main__':
    uvicorn.run("main:app",
                    host="127.0.0.1",
                    port=7700,
                    reload=True,
                    debug=True)

# uvicorn.run(app, host="127.0.0.1", port=8080)
