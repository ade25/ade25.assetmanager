# -*- coding: utf-8 -*-
"""Module providing views for asset listings"""
from Acquisition import aq_inner
from Products.Five.browser import BrowserView


class StackView(BrowserView):
    """ Folderish stack content default view """

    def addable_media_types(self):
        context = aq_inner(self.context)
        return context.getAllowedTypes()


class StackPreview(BrowserView):
    """ Reusable stack preview image """

    def contained_items(self):
        context = aq_inner(self.context)
        items = context.restrictedTraverse('@@folderListing')()
        return items

    def has_contained_items(self):
        return len(self.contained_items()) > 0

    def first_item(self):
        return self.contained_items()[0]
