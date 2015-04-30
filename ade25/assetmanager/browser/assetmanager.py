# -*- coding: utf-8 -*-
"""Module providing asset management views"""

import json
from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from plone import api
from plone.app.blob.interfaces import IATBlobImage

from ade25.assetmanager.stack import IStack


class AssetManagerView(BrowserView):
    """ Central management unit """

    def __call__(self):
        self.has_assets = len(self.assets()) > 0

    def assets(self):
        context = aq_inner(self.context)
        data = getattr(context, 'assets')
        if data is None:
            data = dict()
        return data

    def stored_data(self):
        return json.loads(self.assets())


class SelectStack(BrowserView):
    """ Select asset stack """

    def __call__(self):
        self.has_stacks = len(self.stacks()) > 0

    def stacks(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        stacks = catalog(object_provides=IStack.__identifier__,
                         sort_on='getObjPositionInParent')
        return stacks

    def contained_items(self, uuid):
        stack = api.content.get(UID=uuid)
        return stack.restrictedTraverse('@@folderListing')()

    def item_count(self, uuid):
        return len(self.contained_items(uuid))

    def preview_image(self, uuid):
        images = self.contained_images(uuid)
        preview = None
        if len(images):
            first_item = images[0].getObject()
            if IATBlobImage.providedBy(first_item):
                preview = first_item
        return preview


class SelectAsset(BrowserView):
    """ Select assets from preselected stack """


class AssignAsset(BrowserView):
    """ Assign asset to context specific asset storage """
