# -*- coding: utf-8 -*-
"""Module providing content type for stacks of assets"""

from plone.dexterity.content import Container
from plone.directives import form
from plone.namedfile.interfaces import IImageScaleTraversable
from zope.interface import implementer
from zope import schema

from ade25.assetmanager import _


class IStack(form.Schema, IImageScaleTraversable):
    """
    A folderish content stack
    """
    assignment = schema.TextLine(
        title=_(u"Assigments"),
        description=_(u"JSON formated listing of assignments"),
        required=False,
    )
    form.mode(assignment="hidden")


@implementer(IStack)
class Stack(Container):
    pass
