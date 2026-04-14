import balderhub.auth.lib.utils

from .actions import HttpAction
from .http_resource import HttpResource


class HttpOperation(balderhub.auth.lib.utils.Operation):
    """
    Represents an HTTP operation consisting of a resource and an action.
    """
    def __init__(self, resource: HttpResource, action: HttpAction):

        if not isinstance(resource, HttpResource):
            raise TypeError(f'resource must be of type {HttpResource.__name__}')
        if not isinstance(action, HttpAction):
            raise TypeError(f'action must be of type {HttpAction.__name__}')
        super().__init__(resource, action)

    @property
    def resource(self) -> HttpResource:
        """
        :return: the HTTP resource associated with the operation.
        """
        return self._resource

    @property
    def action(self) -> HttpAction:
        """
        :return: the HTTP action to be performed on the resource.
        """
        return self._action
