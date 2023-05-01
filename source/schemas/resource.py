from pydantic import BaseModel, validator, ValidationError, HttpUrl
from pydantic.types import List
from pydantic.color import Color
import datetime
from source.Enums import Error_msg_resource as Error_msg


class Data(BaseModel):
    id: int
    name: str
    year: int
    color: Color
    pantone_value: str
    @validator('year')
    def check_year(cls, year):
        if year < 1963 and year > datetime.datetime.now().year:   #Pantone Matching System was created in 1963
            raise ValueError(Error_msg.WRONG_YEAR.value)
        else:
            return year

    @validator('id')
    def check_id(cls, id):
        if id < 0:
            raise ValueError(Error_msg.WRONG_ID.value)
        else:
            return id



class Support(BaseModel):
    url: HttpUrl
    text: str

class Resource(BaseModel):
    data: Data
    support: Support

class Not_Data(BaseModel):
    pass

class Resources_list(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Data]
    support: Support
    @validator("page")
    def val_pages(cls, page):
        if page < 1:
            raise ValueError(Error_msg.WRONG_PAGE.value)
        else:
            return page

class Not_Resource(BaseModel):
    pass

class Not_Resources_list(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Not_Data]
    support: Support
