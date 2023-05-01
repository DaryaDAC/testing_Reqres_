from pydantic import BaseModel, validator, ValidationError, HttpUrl, EmailStr
from pydantic.types import List
from source.Enums import Error_msg_user as Error_msg

class Data(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl
    @validator('id')
    def check_id(cls, id):
        if id < 0:
            raise ValueError(Error_msg.WRONG_ID.value) # The requirements for the desired parameter values were not described
        else:
            return id
    @validator('first_name')
    def check_name(cls, first_name):
        if " " in first_name:
            raise ValueError(Error_msg.WRONG_FIRST_NAME) # It is assumed that the first_name consists of one word, and the last_name can be compound
        else:
            return first_name
class Not_Data(BaseModel):
    pass


class Support(BaseModel):
    url: HttpUrl #HttpUrl validator
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

class Not_Users(BaseModel):
    pass

class Not_Users_list(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Not_Data]
    support: Support


