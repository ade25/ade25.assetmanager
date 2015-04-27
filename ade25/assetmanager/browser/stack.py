# -*- coding: utf-8 -*-
"""Module providing views for asset listings"""
from Acquisition import aq_inner
from Products.Five.browser import BrowserView


class StackView(BrowserView):
    """ Folderish stack content default view """

    def addable_media_types(self):
        context = aq_inner(self.context)
        return context.getAllowedTypes()
