# -*- coding: utf-8 -*-
from plone.app.contenttypes import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives as form
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope import schema


@provider(IFormFieldProvider)
class IAssetStorage(model.Schema):

    assets = schema.TextLine(
        title=_(u'Assigned Assets', default=u'Text'),
        description=u"JSON formated listing of asigned assets",
        required=False,
    )
    form.mode(assets='hidden')


@implementer(IAssetStorage)
@adapter(IDexterityContent)
class AssetStorage(object):

    def __init__(self, context):
        self.context = context
