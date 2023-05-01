from pydantic import BaseModel, validator, ValidationError, EmailStr
from pydantic.types import List
from source.Enums import Error_msg_registration as Error_msg

class User_reg_send(BaseModel):
    email: EmailStr
    password: str
    @validator('password')
    def check_password(cls, password):
        if len(password) < 1:
            raise ValueError(Error_msg.WRONG_PASSWORD.value)
        else:
            return password

class User_reg_get_info(BaseModel):
    id: int
    token: str
    @validator('token')
    def check_token(cls, token):
        if len(token) < 1:
            raise ValueError(Error_msg.WRONG_TOKEN.value)
        else:
            return token

class User_get_token(BaseModel):
    token:str
    @validator('token')
    def check_token(cls, token):
        if len(token) < 1:
            raise ValueError(Error_msg.WRONG_TOKEN.value)

class User_reg_error(BaseModel):
    error: str

class User_err(BaseModel):
    pass

class User_create_info(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str

class User_update(BaseModel):
    name: str
    job: str
    updatedAt: str


