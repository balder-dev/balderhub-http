from balderhub.data.contrib.auth.utils import ResourceForSpecificDataItem

from balderhub.data.lib.utils import SingleDataItem
from balderhub.url.lib.utils import Url

from .http_resource import HttpResource
from .unresolved_http_resource import UnresolvedHttpResource

class UnresolvedDataItemHttpResource(ResourceForSpecificDataItem, UnresolvedHttpResource):
    """
    Represents an HTTP resource for unresolved data items within a specific data item type.

    This class combines functionality from the `ResourceForSpecificDataItem` and
    `UnresolvedHttpResource` base classes to handle unresolved HTTP resources.
    It provides mechanisms for resolving the resource into a fully defined HTTP
    resource based on input parameters derived from the specific data item's fields.
    """
    def __init__(self, url_schema: Url, data_item_type: type[SingleDataItem], **kwargs):
        """
        Initialize the unresolved data item http resource.

        :param url_schema: The schema of the URL associated with the resource, containing
        placeholders for parameters to be filled during resolution.
        :param data_item_type: The type of the specific data item this resource is associated
        with, used for dynamic field resolution.
        """
        super().__init__(data_item_type=data_item_type, url_schema=url_schema, **kwargs)

    def __str__(self):
        return f"{self.__class__.__name__}<{self._url_schema}@{self.data_item_type.__name__}>"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.url_schema == other.url_schema and self.data_item_type == other.data_item_type

    def __hash__(self):
        return hash(self.__class__) + hash(self._url_schema) + hash(self.data_item_type)

    def get_resolved_resource(self, param: ResourceForSpecificDataItem.Parameter) -> HttpResource:
        unfilled_params = self._url_schema.get_unfilled_parameters().keys()
        resolved_url = self._url_schema.fill_parameters(
            **{url_param: param.data_item.get_field_value(url_param) for url_param in unfilled_params}
        )
        return HttpResource(resolved_url)
