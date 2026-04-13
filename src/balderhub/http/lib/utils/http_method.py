from enum import Enum

class HttpMethod(Enum):
    """
    This enum describes all common HTTP methods supported by BalderHub.
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
