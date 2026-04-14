from typing import Union

import balderhub.auth.lib.utils
from balderhub.url.lib.utils import Url


class HttpResource(balderhub.auth.lib.utils.Resource):
    """
    Represents an HTTP resource with a URL.

    This class is designed to encapsulate an HTTP resource by managing its URL,
    allowing comparison with other resources of the same type, and providing a
    structured string representation.
    """
    class NotAllowedMethodError(balderhub.auth.lib.utils.Resource.ResourceEnterError):
        """Represents an error raised when a forbidden method is attempted to be used."""

    def __init__(self, url: Union[Url, str]):
        """
        Initialize a HttpResource object.

        :param url: the URL to which the resource is being requested
        """
        super().__init__()
        self._url = url if isinstance(url, Url) else Url(url)

    def __str__(self):
        return f"{self.__class__.__name__}<{self._url}>"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.url == other.url

    def __hash__(self):
        return hash(self.__class__) + hash(self.url)

    @property
    def url(self) -> Url:
        """
        :return: the URL of the HTTP resource
        """
        return self._url
