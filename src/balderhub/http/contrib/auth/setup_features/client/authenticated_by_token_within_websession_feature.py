import balderhub.auth.lib.scenario_features.client.role
import balderhub.http.lib.setup_features.client


class AuthenticatedByTokenWithinWebsessionFeature(balderhub.auth.lib.scenario_features.client.AuthenticationFeature):
    """
    Enables and manages token-based authentication within a web session.

    This feature provides mechanisms to handle token authentication by managing
    the HTTP headers within a web session. The authentication state is verified
    by checking the presence and correctness of a token in the session's headers.
    """
    #: the key name used for the authentication header.
    HEADER_KEY_NAME = 'Authorization'
    #: the prefix added to the token value in the header.
    TOKEN_PREFIX = 'Token'

    #: inner-feature reference to the configuration object for the user's token role.
    user_config = balderhub.auth.lib.scenario_features.client.role.TokenRoleFeature()
    #: inner-feature reference to the web session object where authentication headers
    websession = balderhub.http.lib.setup_features.client.WebSessionWithRequestsFeature()

    def get_full_header_value(self):
        """
        Constructs and returns the full header value by combining the token prefix and
        the user's token.

        :return: A string representing the complete header value, consisting of the
            ``TOKEN_PREFIX`` and the user's token separated by a space.
        """
        return f'{self.TOKEN_PREFIX} {self.user_config.token}'

    @property
    def is_authenticated(self) -> bool:
        return self.HEADER_KEY_NAME in self.websession.session.headers and \
            self.websession.session.headers[self.HEADER_KEY_NAME] == self.get_full_header_value()

    def authenticate(self):
        # TODO provide native method in feature directly to manage header
        self.websession.session.headers[self.HEADER_KEY_NAME] = self.get_full_header_value()

    def unauthenticate(self):
        # TODO provide native method in feature directly to manage header
        del self.websession.session.headers[self.HEADER_KEY_NAME]
