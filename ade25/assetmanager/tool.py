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

    def read(self, uuid, key=None):
        item = api.content.get(UID=uuid)
        stored = getattr(item, 'assets')
        data = json.loads(stored)
        if key is not None:
            records = data['items']
            record = records[0]
            data = record[key]
        return data

    def delete(self, uuid, key=None):
        stored = self.read(uuid)
        if key is not None:
            stored[key] = dict()
            updated = json.dumps(stored)
            item = api.content.get(UID=uuid)
            setattr(item, 'assets', updated)
            modified(item)
            item.reindexObject(idxs='modified')
        return uuid

    def safe_encode(self, value):
        """Return safe unicode version of value.
        """
        su = safe_unicode(value)
        return su.encode('utf-8')
