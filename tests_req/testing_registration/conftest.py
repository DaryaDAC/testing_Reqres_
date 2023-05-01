import pytest
import os
from tests_req.config_path import PATH_REPORT_REGISTRATION

@pytest.fixture(scope="session", autouse=True)
def re_path_report():
    for f in os.listdir(PATH_REPORT_REGISTRATION):
        os.remove(os.path.join(PATH_REPORT_REGISTRATION, f))
