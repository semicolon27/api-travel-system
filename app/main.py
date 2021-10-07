from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
import uvicorn
from app.models import db_models
from app.routers.master import product_router, city_router, category_router, country_router, currency_router, division_router, jobkind_router, office_router
from app.database import SessionLocal, engine
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True, title="Travel System API")
# app = FastAPI(debug=False, title="Travel System API", docs_url=None, redoc_url=None, openapi_url=None)

origins = [
    "http://localhost:8080",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(product_router.router)
app.include_router(city_router.router)
app.include_router(category_router.router)
app.include_router(country_router.router)
app.include_router(currency_router.router)
app.include_router(division_router.router)
app.include_router(jobkind_router.router)
app.include_router(office_router.router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(_, exc):
    # print(exc.errors())
    res = {}
    res['rc'] = '999'
    res['msg'] = "Error"
    res.data = {}
    # res.data = {"detail": exc.errors(), "body": exc.body}
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(res),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_, exc):
    print(exc.errors())
    res = {}
    res['rc'] = '422'
    res['msg'] = "Bad Request"
    res['data'] = {}
    # res['data'] = {"detail": exc.errors(), "body": exc.body}
    # return Response(res, status_code=400)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=res,
    )

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=7700,
                reload=True,
                debug=True)
