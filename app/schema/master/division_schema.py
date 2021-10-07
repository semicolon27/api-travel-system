from pydantic import BaseModel


class Division(BaseModel):
    OffCode: str
    DivID: str
    DivName: str

    class Config:
        orm_mode = True


class RequestDivisionByCode(BaseModel):
    OffCode: str
    varselection: str
    varlong: int
