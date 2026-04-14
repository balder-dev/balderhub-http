from __future__ import annotations

import balderhub.auth.lib.scenario_features.server
from balderhub.auth.lib.utils import ResourceRule, ResourceRuleList

from balderhub.http.contrib.auth.utils import actions
from ...utils import UnresolvedHttpResource
from ...utils.functions import get_reverse_rule_cb_for
from ...utils.http_resource import HttpResource

class SimpleHttpExistForConfig(balderhub.auth.lib.scenario_features.server.ExistenceForConfig):
    """
    This existence-for configuration feature automatically determines non-existing resources by creating a resource for
    every normal HttpMethod and Url, that is used in
    :meth:`balderhub.auth.lib.scenario_features.server.ExistenceForConfig.resources_that_exist`.

    Subclasses can overwrite the method :meth:`HttpExistenceForConfig.additional_non_existing_resources` to add
    additional resources that should be tested.
    """
    USE_HTTP_ACTIONS = [actions.GET, actions.POST, actions.PUT, actions.PATCH, actions.DELETE]

    def get_resource_rules_that_exist(self) -> ResourceRuleList:
        raise NotImplementedError

    def get_resource_rules_that_not_exist(self) -> ResourceRuleList:
        existing_rules = self.get_resource_rules_that_exist()

        result = []

        resolved_resources_dict = {}
        for cur_existing_rule in existing_rules:
            resource = cur_existing_rule.resource
            if isinstance(resource, HttpResource):
                if resource.url not in resolved_resources_dict.keys():
                    resolved_resources_dict[resource.url] = []
                for action in cur_existing_rule.actions:
                    resolved_resources_dict[resource.url].append(action)
            elif isinstance(resource, UnresolvedHttpResource):
                cur_rule = cur_existing_rule.cb_rule
                # otherwise rule is none -> every item is active - no item is in reverse-rule
                if cur_rule:
                    reverse_rule = get_reverse_rule_cb_for(cur_rule)
                    new_rule = cur_existing_rule.copy()
                    new_rule.update_rule(reverse_rule)
                    result.append(new_rule)
            else:
                raise TypeError(f'unexpected resource type `{type(resource)}`')

        for resource_url, existing_actions in resolved_resources_dict.items():
            not_existing_actions = list(set(self.USE_HTTP_ACTIONS) - set(existing_actions))
            if len(not_existing_actions) > 0:
                result.append(ResourceRule(HttpResource(resource_url), actions=not_existing_actions))
        return ResourceRuleList(result)
