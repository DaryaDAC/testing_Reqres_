from enum import Enum

class Error_msg(Enum):
    WRONG_STATUS_CODE = "Status code is not expected"
    WRONG_YEAR = "Invalid year"
    WRONG_ID = "Invalid ID"
    WRONG_PAGE = "Invalid page"