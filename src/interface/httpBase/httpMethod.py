from enum import Enum, unique


@unique
class MethodEnum(Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'
