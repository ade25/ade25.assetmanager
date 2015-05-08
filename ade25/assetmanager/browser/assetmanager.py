# -*- coding: utf-8 -*-
"""Module providing asset management views"""

import json
import uuid as uuid_tool

from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from plone import api
from plone.app.blob.interfaces import IATBlobImage
from zope.component import getUtility
from zope.lifecycleevent import modified

from ade25.assetmanager.interfaces import IAssetAssignmentTool
from ade25.assetmanager.stack import IStack


class AssetManagerView(BrowserView):
    """ Central management unit """

    def __call__(self):
        self.has_assets = len(self.assets()) > 0
        return self.render()

    def render(self):
        return self.index()

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

    def stacks(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        stacks = catalog(object_provides=IStack.__identifier__,
                         sort_on='getObjPositionInParent')
        return stacks

    def has_stacks(self):
        return len(self.stacks()) > 0

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

    def __call__(self):
        self.has_assets = len(self.contained_assets()) > 0
        return self.render()

    def render(self):
        return self.index()

    @property
    def traverse_subpath(self):
        return self.subpath

    def publishTraverse(self, request, name):
        if not hasattr(self, 'subpath'):
            self.subpath = []
        self.subpath.append(name)
        return self

    def contained_assets(self):
        uid = self.traverse_subpath[0]
        stack = api.content.get(UID=uid)
        images = stack.restrictedTraverse('@@folderListing')()
        return images


class AssignAsset(BrowserView):
    """ Assign asset to context specific asset storage """

    def __call__(self):
        return self.render()

    @property
    def traverse_subpath(self):
        return self.subpath

    def publishTraverse(self, request, name):
        if not hasattr(self, 'subpath'):
            self.subpath = []
        self.subpath.append(name)
        return self

    def render(self):
        context = aq_inner(self.context)
        base_url = context.absolute_url()
        stack = self.traverse_subpath[0]
        next_url = '{0}/@@select-asset/{1}'.format(base_url, stack)
        uuid = self._add_item()
        self._propagate('update', uuid)
        return self.request.response.redirect(next_url)

    def assets(self):
        context = aq_inner(self.context)
        data = getattr(context, 'assets')
        if data is None:
            tool = getUtility(IAssetAssignmentTool)
            data = tool.create()
        return data

    def stored_data(self):
        return json.loads(self.assets())

    def _add_item(self):
        data = self.stored_data()
        uid = self.traverse_subpath[1]
        items = data['items']
        item = {
            'id': uuid_tool.uuid4(),
            'uid': uid,
            'caption': ''
        }
        items.append(item)
        data['items'] = items
        tool = getUtility(IAssetAssignmentTool)
        context = aq_inner(self.context)
        context_uid = api.content.get_uuid(obj=context)
        data = tool.update(context_uid, data)
        return data

    def _propagate(self, action, uuid):
        pid = self.project_uid()
        stack = api.content.get(UID=uuid)
        assignments = getattr(stack, 'assignments')
        plist = list()
        if assignments is not None:
            plist = json.loads(assignments)
        if action == 'delete' and len(plist):
            plist.remove(pid)
        else:
            plist.append(pid)
        setattr(stack, 'assignments', json.dumps(plist))
        modified(stack)
        stack.reindexObject(idxs='modified')
        return 'success'
