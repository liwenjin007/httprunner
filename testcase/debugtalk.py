import os
import uuid
from httprunner import __version__


def gen_random_request_id():
    return str(uuid.uuid4())


def get_httprunner_version():
    return __version__


def get_test_env():
    if os.environ.get("TestEnv") == "prod":
        return "mubu.net"
    else:
        return "mubu.com"
