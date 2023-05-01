from pydantic import BaseModel, validator, EmailStr
from source.Enums import Error_msg_registration as Error_msg

class User_reg_send(BaseModel):
    email: EmailStr
    password: str
    @validator('password')
    def check_password(cls, password):
        if len(password) < 1:
            raise ValueError(Error_msg.WRONG_PASSWORD.value) # The requirements for the desired parameter values were not described (len(psw) - ?)
        else:
            return password

class User_reg_get_info(BaseModel):
    id: int
    token: str
    @validator('token')
    def check_token(cls, token):
        if len(token) < 1:
            raise ValueError(Error_msg.WRONG_TOKEN.value) # The requirements for the desired parameter values were not described
        else:
            return token
    @validator('id')
    def check_id(cls, id):
        if id < 0:
            raise ValueError(Error_msg.WRONG_ID.value)

class User_get_token(BaseModel):
    token:str
    @validator('token')
    def check_token(cls, token):
        if len(token) < 1:
            raise ValueError(Error_msg.WRONG_TOKEN.value) # The requirements for the desired parameter values were not described

class User_reg_error(BaseModel):
    error: str

class User_err(BaseModel):
    pass

class User_create_info(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str
    @validator('id')
    def check_id(cls, id):
        if int(id) < 0:
            raise ValueError(Error_msg.WRONG_ID.value) # The requirements for the desired parameter values were not described (str(id) - ?)

class User_update(BaseModel):
    name: str
    job: str
    updatedAt: str


