from pydantic import BaseModel


class JobKind(BaseModel):
    OffCode: str
    JobKind: str
    JobName: str
    DivID: str

    class Config:
        orm_mode = True
