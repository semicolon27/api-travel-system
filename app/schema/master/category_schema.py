from pydantic import BaseModel


class Category(BaseModel):
    CategoryID: str
    CategoryDesc: str

    class Config:
        orm_mode = True
