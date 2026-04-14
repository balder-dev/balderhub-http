from abc import ABC
import balderhub.auth.lib.utils
from balderhub.url.lib.utils import Url


class UnresolvedHttpResource(balderhub.auth.lib.utils.UnresolvedResource, ABC):
    """
    Represents an HTTP resource with an unresolved schema.

    This class is used to manage and represent HTTP resources where the schema
    (such as URL structure) is not fully resolved. It provides utility methods
    for equality comparison, string representation, and hashing based on the
    URL schema. It inherits from `UnresolvedResource` and ensures compatibility
    with existing resource utilities.
    """
    class NotAllowedMethodError(balderhub.auth.lib.utils.Resource.ResourceEnterError):
        """
        Represents an error raised when a method is not allowed for a specific
        resource or context.
        """

    def __init__(self, url_schema: Url, **kwargs):
        """
        Initiates an unresolved HTTP resource

        :param url_schema: represents the unresolved URL schema
        """
        super().__init__(**kwargs)
        self._url_schema = url_schema

    def __str__(self):
        return f"{self.__class__.__name__}<{self._url_schema}>"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.url_schema == other.url_schema

    def __hash__(self):
        return hash(self.__class__) + hash(self._url_schema)

    @property
    def url_schema(self):
        """
        :return: represents the unresolved URL schema for the resource
        """
        return self._url_schema
