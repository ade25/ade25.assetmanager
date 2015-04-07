# -*- coding: utf-8 -*-
"""Module providing ContentPage content type functionality"""

from plone.dexterity.content import Container
from plone.directives import form
from plone.namedfile.interfaces import IImageScaleTraversable
from zope.interface import implementer

from ade25.assetmanager import MessageFactory as _


class IAssetRepository(form.Schema, IImageScaleTraversable):
    """
    A folderish page
    """


@implementer(IAssetRepository)
class AssetRepository(Container):
    pass
