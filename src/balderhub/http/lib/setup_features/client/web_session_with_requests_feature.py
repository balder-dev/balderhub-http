from __future__ import annotations

import requests
from balderhub.url.lib.utils import Url
from ...utils.functions import convert_requests_response
from ...utils.response import Response
from ...utils.http_method import HttpMethod
from ...scenario_features.client.web_session_feature import WebSessionFeature


class WebSessionWithRequestsFeature(WebSessionFeature):
    """
    This setup feature provides an implementation for working with web session by using the python-requests library.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session = requests.Session()

    def request(
            self,
            method: str | HttpMethod,
            url: str | Url,
            data: dict | bytes | None = None,
            headers: dict[str, str] | None = None,
            cookies: dict[str, str] | None = None,
            **kwargs
    ) -> Response:
        method_as_str = method.value if isinstance(method, HttpMethod) else method
        if data is None:
            data = {}

        session_response = self.session.request(
            method=method_as_str,
            url=str(url),
            data=data,
            headers=headers,
            cookies=cookies
        )
        response = convert_requests_response(session_response)
        self._responses.append(response)
        return response
