from typing import Union

from balderhub.auth.lib.utils import Action

from balderhub.http.lib.utils import HttpMethod


class HttpAction(Action):
    """
    Represents an HTTP method implementing the :class:`balderhub.auth.lib.utils.Action` interface.
    """
    def __init__(self, method: Union[HttpMethod, str]):
        super().__init__()
        self._method_str = method if isinstance(method, str) else method.value

    def __str__(self):
        return f"HttpAction<{self._method_str}>"

    def __hash__(self):
        return hash(self.__class__) + hash(self._method_str)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.http_method == other.http_method

    @property
    def http_method(self) -> str:
        """
        :return: the HTTP method associated with this action, as a string.
        """
        return self._method_str


GET = HttpAction('GET')
POST = HttpAction('POST')
PUT = HttpAction('PUT')
PATCH = HttpAction('PATCH')
DELETE = HttpAction('DELETE')
HEAD = HttpAction('HEAD')
OPTIONS = HttpAction('OPTIONS')
TRACE = HttpAction('TRACE')
