from pydantic import BaseModel


class BranchOffice(BaseModel):
    OffCode: str
    CompanyID: str
    CityID: str
    name: str

    class Config:
        orm_mode = True
