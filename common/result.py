import json


class Result:

    @classmethod
    def ok(cls, data=None):
        return json.dumps({
            "code": 0,
            "data": data,
            "message": ""
        })

    @classmethod
    def error(cls, message=""):
        return json.dumps({
            "code": -1,
            "data": None,
            "message": message
        })

    @classmethod
    def logout(cls):
        return json.dumps({
            "code": -2,
            "data": None,
            "message": "登录已失效"
        })