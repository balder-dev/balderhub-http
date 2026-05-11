Examples
********

This package provides a feature to interact by a session-based web session. It also provides a ready-to-use
implementation with :class:`balderhub.http.lib.setup_features.client.WebSessionWithRequestsFeature` using the
`python requests package <https://github.com/psf/requests>`_.

.. note::
    If you want to implement permission / authentification tests, have a look into the
    `contrib section of this documentation <Contrib for \`\`balderhub-auth\`\`>`_.

Creating universal Scenarios
============================

If you need a web session within a test scenario, you can use the
:class:`balderhub.http.lib.scenario_features.client.WebSessionFeature` like shown below:

.. code-block:: python

    from balderhub.http.lib.utils import HttpMethod

    class ScenarioExample(balder.Scenario):

        class WebSessionDevice(balder.Device):
            web = balderhub.http.lib.scenario_features.client.WebSessionFeature()
            ...

        def test_check_website(self):
            response = self.WebSessionDevice.web.request(HttpMethod.GET, "https://docs.balder.dev")
            assert response.status_code == 200, response

Using it in Setups
==================

You can use a ready-to-use implementation for the :class:`balderhub.http.lib.scenario_features.client.WebSessionFeature`
with the shipped :class:`balderhub.http.lib.setup_features.client.WebSessionWithRequestsFeature`:


.. code-block:: python

    from balderhub.http.lib.utils import HttpMethod

    class SetupWithRequests(balder.Scenario):

        class Client(balder.Device):
            web = balderhub.http.lib.setup_features.client.WebSessionWithRequestsFeature()
            ...
