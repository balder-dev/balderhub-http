from __future__ import annotations
import dataclasses

from balderhub.url.lib.utils import Url



@dataclasses.dataclass
class Response:
    """
    Represents an HTTP response received from a request made to a specific URL.

    This class encapsulates the details of an HTTP response, including the status code,
    the URL from which the response was received, the content of the response, and the
    history of any preceding responses (e.g., in cases of redirects or retries).

    :ivar status_code: Status code returned by the server.
    :type status_code: int
    :ivar url: The URL from which the response was received.
    :type url: Url
    :ivar content: The raw binary content of the response.
    :type content: bytes
    :ivar history: List of preceding Response objects that represent the redirection
        or retry history leading to this response. Defaults to an empty list.
    :type history: list[Response]
    """
    status_code: int
    url: Url
    content: bytes
    history: list[Response] = dataclasses.field(default_factory=list)
