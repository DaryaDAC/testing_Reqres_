from pydantic import BaseModel, validator, ValidationError

class Data(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class Support(BaseModel):
    url: str
    text: str

class User(BaseModel):
    data: Data
    support: Support

# {
#     "data": {
#         "id": 2,
#         "email": "janet.weaver@reqres.in",
#         "first_name": "Janet",
#         "last_name": "Weaver",
#         "avatar": "https://reqres.in/img/faces/2-image.jpg"
#     },
#     "support": {
#         "url": "https://reqres.in/#support-heading",
#         "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
#     }
# }