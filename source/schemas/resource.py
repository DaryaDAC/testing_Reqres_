from pydantic import BaseModel, validator, ValidationError, HttpUrl
from pydantic.types import List
from pydantic.color import Color


class Data(BaseModel):
    id: int
    name: str
    year: int
    color: Color
    pantone_value: str

class Support(BaseModel):
    url: HttpUrl
    text: str

class Resource(BaseModel):
    data: Data
    support: Support
