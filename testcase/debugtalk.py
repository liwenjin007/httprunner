import os
import uuid
from httprunner import __version__
from httprunner.response import ResponseObject


def gen_random_request_id():
    return str(uuid.uuid4())


def get_httprunner_version():
    return __version__


def get_test_env():
    if os.environ.get("TestEnv") == "prod":
        return "mubu.net"
    else:
        return "mubu.com"


def get_response(resp:ResponseObject):
    print(f"resp______")
    resp = resp.resp_obj.json()
    print(resp["data"])
    return resp["data"]["phone"]
