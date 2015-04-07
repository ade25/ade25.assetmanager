# -*- coding: utf-8 -*-
"""Module providing asset management views"""

import json
from Acquisition import aq_inner
from Products.Five.browser import BrowserView


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
