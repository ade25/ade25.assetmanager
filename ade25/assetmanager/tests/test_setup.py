# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from ade25.assetmanager.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of ade25.assetmanager into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ade25.assetmanager is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('ade25.assetmanager'))

    def test_uninstall(self):
        """Test if ade25.assetmanager is cleanly uninstalled."""
        self.installer.uninstallProducts(['ade25.assetmanager'])
        self.assertFalse(self.installer.isProductInstalled('ade25.assetmanager'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IAde25AssetmanagerLayer is registered."""
        from ade25.assetmanager.interfaces import IAde25AssetmanagerLayer
        from plone.browserlayer import utils
        self.failUnless(IAde25AssetmanagerLayer in utils.registered_layers())
