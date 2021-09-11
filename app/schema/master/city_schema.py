from pydantic import BaseModel


class City(BaseModel):
    CityID: str
    Name: str
    countryID: str
    locKind: str

    class Config:
        orm_mode = True
