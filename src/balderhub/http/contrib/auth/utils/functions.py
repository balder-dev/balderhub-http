from collections.abc import Callable

from balderhub.auth.lib.utils.unresolved_resource import UnresolvedResource


def get_reverse_rule_cb_for(
        rule: Callable[[UnresolvedResource.Parameter], bool]
) -> Callable[[UnresolvedResource.Parameter], bool]:
    """
    Returns a callable function that inverses the logic of the provided rule, 
    which takes an argument and returns the opposite boolean value.

    :param rule: A callable function that takes an instance of 
        ``UnresolvedResource.Parameter`` as input and returns a boolean value.
    :return: A callable function that applies the inverse logic of the 
        provided ``rule`` on an instance of ``UnresolvedResource.Parameter``.
    :raises ValueError: If rule is not a callable object.
    """
    if not callable(rule):
        raise ValueError(f'rule must be callable, but is {rule}')
    return lambda x: not rule(x)
