# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface


class IAde25AssetmanagerLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IAssetManagerEnabled(Interface):
    """ Marker interface for asset manager enabled content """


class IAssetAssignmentTool(Interface):
    """ Asset manager data processing

        General tool providingCRUD operations for assigning assets
        to content object implementing the IAssetManagerEnabled
        marker interface
    """

    def create(context):
        """ Create asset assignment data file

        The caller is responsible for passing a valid data dictionary
        containing the necessary details

        Returns processing status codes SUCCESS/ERROR

        @param uuid:        caravan site object UID
        @param data:        predefined initial data dictionary
        """

    def read(context):
        """ Read stored data from carvan site object

        Returns a dictionary

        @param uuid:        caravan site object UID
        @param key:         (optional) dictionary item key
        """

    def update(context):
        """ Read stored data from carvan site object

        Returns a dictionary

        @param uuid:        caravan site object UID
        @param key:         (optional) dictionary item key
        @param data:        data dictionary
        """

    def delete(context):
        """ Read stored data from carvan site object

        Returns a dictionary

        @param uuid:        caravan site object UID
        @param key:         (optional) dictionary item key
        """
