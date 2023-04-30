from pydantic import BaseModel, validator, ValidationError, EmailStr
from pydantic.types import List

class User_reg_send(BaseModel):
    email: EmailStr
    password: str

class User_reg_get_info(BaseModel):
    id: int
    token: str