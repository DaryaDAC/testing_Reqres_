from enum import Enum

class Error_msg(Enum):
    WRONG_STATUS_CODE = "Status code is not expected"
    WRONG_YEAR = "Invalid year"
    WRONG_ID = "Invalid ID"
    WRONG_PAGE = "Invalid page"

class Error_msg_registration(Enum):
    WRONG_TOKEN = "Invalid token. Token length is less than 1"
    WRONG_PASSWORD = "Invalid password. Password length is less than 1"
