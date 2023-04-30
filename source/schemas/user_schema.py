from pydantic import BaseModel, validator, ValidationError, HttpUrl, EmailStr
from pydantic.types import List

class Data(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl

class Support(BaseModel):
    url: HttpUrl
    text: str

class User(BaseModel):
    data: Data
    support: Support

class Users_list(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Data]
    support: Support

