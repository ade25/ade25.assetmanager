# -*- coding: utf-8 -*-
"""Module providing JSON storage for static asset assignments"""
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives as form
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope import schema

from ade25.assetmanager import _


@provider(IFormFieldProvider)
class IAssetStorage(model.Schema):

    assets = schema.TextLine(
        title=_(u"Assigned Assets"),
        description=_(u"JSON formated listing of asigned assets"),
        required=False,
    )
    form.mode(assets="hidden")


@implementer(IAssetStorage)
@adapter(IDexterityContent)
class AssetStorage(object):

    def __init__(self, context):
        self.context = context
