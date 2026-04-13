import requests

from balderhub.url.lib.utils import Url


from .response import Response

def convert_requests_response(response: requests.Response) -> Response:
    """
    Converts a `requests.Response` object into the BalderHub `Response` object.

    :param response: A `requests.Response` object that contains metadata, content,
        and history of the HTTP request/response cycle.
    :return: A transformed `Response` object containing the status code, URL,
        content, and processed history of the `requests.Response`.
    """
    history = []
    for cur_history in response.history:
        history.append(
            Response(
                status_code=cur_history.status_code,
                url=Url(cur_history.url),
                content=cur_history.content)
        )
    return Response(
        status_code=response.status_code,
        url=Url(response.url),
        history=history,
        content=response.content
    )
