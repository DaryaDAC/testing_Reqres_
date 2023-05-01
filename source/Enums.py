from enum import Enum

class Error_msg(Enum):
    WRONG_STATUS_CODE = "Status code is not expected"

class Error_msg_registration(Enum):
    WRONG_TOKEN = "Invalid token. Token length is less than 1"
    WRONG_PASSWORD = "Invalid password. Password length is less than 1"
    WRONG_ID = "Invalid ID. ID < 0"

class Error_msg_resource(Enum):
    WRONG_YEAR = "Invalid year"
    WRONG_ID = "Invalid ID"
    WRONG_PAGE = "Invalid page"

class Error_msg_user(Enum):
    WRONG_ID = "Invalid ID"
    WRONG_PAGE = "Invalid page"
    WRONG_FIRST_NAME = "Invalid first name. The first name must not contain spaces"


