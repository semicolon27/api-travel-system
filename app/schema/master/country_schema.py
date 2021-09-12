from pydantic import BaseModel


class Country(BaseModel):
    CountryID: str
    Name: str

    class Config:
        orm_mode = True
