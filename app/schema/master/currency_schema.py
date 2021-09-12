from pydantic import BaseModel


class Currency(BaseModel):
    Cur: str
    Name: str
    CountryID: str
    Rate: int
    Mark: str

    class Config:
        orm_mode = True
