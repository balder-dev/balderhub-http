from balderhub.url.lib.utils import Url

from balderhub.http.lib.utils import HttpMethod


class HttpRequestMessage:
    """Represents an HTTP request message consisting of a URL and an HTTP method.

    This class encapsulates the essential parts of an HTTP request.

    :param url: The target URL for the HTTP request.
    :param method: The HTTP method to be used for the request.
    """

    def __init__(self, url: Url, method: HttpMethod):
        """Initialize the HTTP request message.

        :param url: The target URL for the HTTP request.
        :param method: The HTTP method to be used for the request.
        """
        self._url = url
        self._method = method

    def __eq__(self, other):
        """Check equality with another object.

        Two :class:`HttpRequestMessage` instances are considered equal if they have the same URL and HTTP method.

        :param other: The object to compare with.
        :return: ``True`` if both instances have the same URL and method, ``False`` otherwise.
        """
        if not isinstance(other, HttpRequestMessage):
            return False
        return self._url == other._url and self._method == other._method

    @property
    def url(self) -> Url:
        """The target URL for the HTTP request."""
        return self._url

    @property
    def method(self) -> HttpMethod:
        """The HTTP method to be used for the request."""
        return self._method
