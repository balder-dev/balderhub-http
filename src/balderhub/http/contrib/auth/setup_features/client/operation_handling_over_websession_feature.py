import balderhub.auth.lib.scenario_features.client
from balderhub.auth.lib.utils import Operation
from balderhub.url.lib.utils import Url

from balderhub.http.contrib.auth.utils.actions import HttpAction
from balderhub.http.contrib.auth.utils.http_resource import HttpResource
from balderhub.http.lib.scenario_features.client.web_session_feature import WebSessionFeature


class OperationHandlingOverWebsessionFeature(balderhub.auth.lib.scenario_features.client.OperationHandlingFeature):
    """
    Setup-Level Feature implementation of the
    :class:`balderhub.auth.lib.scenario_features.client.OperationHandlingFeature`. It can be used to test
    authentification / permissions for http resources by using the
    :class:`balderhub.http.lib.scenario_features.client.WebSessionFeature`.
    """
    #: inner feature reference to the web session feature
    websession = WebSessionFeature()

    @property
    def unauth_redirect_schema(self) -> list[Url]:
        """
        This property provides the schema used for unauthenticated redirect URLs.
        It describes a list of Url schemas that are treated the same as an
        Unauthenticated error.

        :return: a list of `Url` objects representing the schema for unauthenticated
            redirects (empty list by default).
        """
        return []

    def enter_operation(self, operation: Operation) -> bool:
        resource = operation.resource
        action = operation.action
        if not isinstance(resource, HttpResource):
            raise TypeError(f'can not operation with resource from type `{resource.__class__}`'
                            f' - this feature only work with resources from type `{HttpResource.__name__}`')
        if not isinstance(action, HttpAction):
            raise TypeError(f'expect http action type `{HttpAction.__name__}`, '
                            f'got {type(action)} instead')

        response = self.websession.request(method=action.http_method, url=resource.url)  # TODO should we send data?

        if len(response.history) > 0:
            # all history elements need to have status code 302
            if {r.status_code for r in response.history} != {302}:
                raise ValueError(f'got non 302 status codes in history responses: {response.history}')

            if self.unauth_redirect_schema:
                # redirects to provided schema should be handled as unauth error too
                for cur_schema in self.unauth_redirect_schema:

                    if cur_schema.compare(response.url, allow_schemas=True):
                        # redirect to login page happened -> return UnauthorizedError
                        raise HttpResource.UnauthorizedError(
                            f'web request has an redirect to unauth URL schema `{cur_schema}`'
                        )
            return False

        if response.status_code == 401:
            raise HttpResource.UnauthorizedError(f'web request returned 401: `{response.content}`')
        if response.status_code == 403:
            raise HttpResource.NoPermissionError(f'web request returned 403: `{response.content}`')
        if response.status_code == 404:
            raise HttpResource.DoesNotExistError(f'web request returned 404: `{response.content}`')
        if response.status_code == 405:
            raise HttpResource.NotAllowedMethodError(f'web request returned 405: `{response.content}`')
        if response.status_code != 200:
            raise HttpResource.ResourceEnterError(f'web request returned unexpected status code '
                                                  f'{response.status_code}: `{response.content}`')
        return True


    def leave_operation(self, operation: Operation) -> bool:
        return True
