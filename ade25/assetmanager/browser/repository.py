# -*- coding: utf-8 -*-
"""Module providing views for asset storage folder"""
from Products.Five.browser import BrowserView
from plone import api
from plone.app.blob.interfaces import IATBlobImage


class AssetRepositoryView(BrowserView):
    """ Folderish content page default view """

    def contained_items(self, uid):
        stack = api.content.get(UID=uid)
        return stack.restrictedTraverse('@@folderListing')()

    def item_index(self, uid):
        return len(self.contained_items(uid))

    def preview_image(self, uid):
        images = self.contained_items(uid)
        preview = None
        if len(images):
            first_item = images[0].getObject()
            if IATBlobImage.providedBy(first_item):
                preview = first_item
        return preview
