from pydantic import BaseModel


class Category(BaseModel):
    CategoryID: str
    CategoryDesc: str
    # kalau ngga pake orm_mode, bakalan value is not a valid dict (type=type_error.dict)
    # khusus skema untuk convert dari hasil query ke respon

    class Config:
        orm_mode = True
