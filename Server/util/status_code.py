from enum import Enum

# 実装するステータスコード定義

STATUS_CODES = {
    'OK': 200,
    'BAD_REQUEST': 400,
    'NOT_FOUND': 404,
    'METHOD_NOT_ALLOWED': 405,
    'URI_TOO_LONG': 414,
    'INTERNAL_SERVER_ERROR': 500
}

class HttpStatus(Enum):
    OK = STATUS_CODES['OK']
    BAD_REQUEST = STATUS_CODES['BAD_REQUEST']
    NOT_FOUND = STATUS_CODES['NOT_FOUND']
    METHOD_NOT_ALLOWED = STATUS_CODES['METHOD_NOT_ALLOWED']
    URI_Too_Long = STATUS_CODES['URI_TOO_LONG']
    INTERNAL_SERVER_ERROR = STATUS_CODES['INTERNAL_SERVER_ERROR']

# 使用例
# print(HttpStatus.OK.value)  # 200 を出力
