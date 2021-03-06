from typing import Generic, Optional, Type, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class Response(GenericModel, Generic[DataT]):
    rc: str = "000"
    msg: str = "Success"
    data: Optional[DataT]
    # kalau ngga pake orm_mode, bakalan value is not a valid dict (type=type_error.dict)
    # khusus skema untuk convert dari hasil query ke respon

    class Config:
        orm_mode = True
