from __future__ import annotations
import balder
from balderhub.url.lib.utils import Url
from balderhub.http.lib.utils import HttpMethod, Response


class WebSessionFeature(balder.Feature):
    """
    Basic feature to work with web sessions.
    """

    def __init__(self, **kwargs: balder.Feature) -> None:
        super().__init__(**kwargs)

        self._responses = []

    def request(
            self,
            method: str | HttpMethod,
            url: str | Url,
            data: dict | bytes | None = None,
            headers: dict[str, str] | None = None,
            cookies: dict[str, str] | None = None,
            **kwargs
    ) -> Response:
        """
        This method allows to execute a request. It returns a new response object.

        :param method: the http method to use
        :param url: the url the request should be made to
        :param data: optional the data that should be append into the body of the request
        :param headers: the headers that the request should include
        :param cookies: the cookies that the request should include
        :return: a response object that holds status code and the answer from the resource
        """
        raise NotImplementedError

    def get_last_response(self) -> Response | None:
        """
        :return: returns the last response that was made over this session
        """
        return self._responses[-1] if len(self._responses) > 0 else None
