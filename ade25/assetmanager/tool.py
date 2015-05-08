# -*- coding: utf-8 -*-
"""Module providing an image asset asignment factory."""
import json
import time
from plone import api
from Products.CMFPlone.utils import safe_unicode
from zope.lifecycleevent import modified


class AssetAssignmentTool(object):
    """ Factory providing CRUD oparations for project assets """

    def create(self, uuid, data):
        item = api.content.get(UID=uuid)
        start = time.time()
        initial_data = self._create_record(uuid, data)
        end = time.time()
        initial_data.update(dict(_runtime=end-start))
        json_data = json.dumps(initial_data)
        setattr(item, 'assets', json_data)
        modified(item)
        item.reindexObject(idxs='modified')
        return uuid

    def safe_encode(self, value):
        """Return safe unicode version of value.
        """
        su = safe_unicode(value)
        return su.encode('utf-8')
