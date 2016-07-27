# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.business_casual.testing import PLONETHEME_BUSINESS_CASUAL_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.business_casual is properly installed."""

    layer = PLONETHEME_BUSINESS_CASUAL_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.business_casual is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.business_casual'))

    def test_browserlayer(self):
        """Test that IPlonethemeBusinessCasualLayer is registered."""
        from plonetheme.business_casual.interfaces import (
            IPlonethemeBusinessCasualLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeBusinessCasualLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_BUSINESS_CASUAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.business_casual'])

    def test_product_uninstalled(self):
        """Test if plonetheme.business_casual is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.business_casual'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeBusinessCasualLayer is removed."""
        from plonetheme.business_casual.interfaces import IPlonethemeBusinessCasualLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeBusinessCasualLayer, utils.registered_layers())
