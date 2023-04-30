from source.Enums import Error_msg

class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.parsed_obj = None

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_obj = schema.parse_obj(item)
                self.parsed_obj = parsed_obj
        else:
            schema.parse_obj(self.response_json)

    def assert_status(self, status):
        if isinstance(status, list):
            assert self.response_status in status, Error_msg.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status, Error_msg.WRONG_STATUS_CODE.value
        return self

    def get_pars_obj(self):
        return self.parsed_obj
