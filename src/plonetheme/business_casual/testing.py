# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.business_casual


class PlonethemeBusinessCasualLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.business_casual)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.business_casual:default')


PLONETHEME_BUSINESS_CASUAL_FIXTURE = PlonethemeBusinessCasualLayer()


PLONETHEME_BUSINESS_CASUAL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_BUSINESS_CASUAL_FIXTURE,),
    name='PlonethemeBusinessCasualLayer:IntegrationTesting'
)


PLONETHEME_BUSINESS_CASUAL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_BUSINESS_CASUAL_FIXTURE,),
    name='PlonethemeBusinessCasualLayer:FunctionalTesting'
)


PLONETHEME_BUSINESS_CASUAL_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_BUSINESS_CASUAL_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeBusinessCasualLayer:AcceptanceTesting'
)
