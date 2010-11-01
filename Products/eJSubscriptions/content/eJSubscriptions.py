# -*- coding: utf-8 -*-
#
# File: eJSubscriptions.py
#
# Copyright (c) 2006 by Kai Diefenbach - iqplusplus
# Generator: ArchGenXML Version 1.5.0 svn/devel
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Kai Diefenbach - iqplusplus <kai.diefenbach <at> iqpp.de>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
import zope
from Products.ATContentTypes.content.folder import ATFolder
from Products.eJSubscriptions.interfaces.IeJSubscriptions import IeJSubscriptions
from Products.eJSubscriptions.config import *

##code-section module-header #fill in your manual code here
from Products.CMFCore import permissions as CMFCorePermissions
##/code-section module-header

schema = Schema((

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

eJSubscriptions_schema = BaseFolderSchema.copy() + \
    getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
eJSubscriptions_schema.moveField('excludeFromNav', after='allowDiscussion')
##/code-section after-schema

class eJSubscriptions(ATFolder, BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(ATFolder,'__implements__',()),) + (getattr(BaseFolder,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IeJSubscriptions)

    # This name appears in the 'add' box
    archetype_name = 'eJSubscriptions'

    meta_type = 'eJSubscriptions'
    portal_type = 'eJSubscriptions'
    allowed_content_types = ['eJSubscriber'] + list(getattr(ATFolder, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 1
    #content_icon = 'eJSubscriptions.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "eJSubscriptions"
    typeDescMsgId = 'description_edit_ejsubscriptions'

    _at_rename_after_creation = True

    schema = eJSubscriptions_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def initializeArchetype(self, **kwargs):
        """
        """
        ATFolder.initializeArchetype(self, **kwargs)
        self.manage_permission(CMFCorePermissions.AddPortalContent, roles=["Anonymous", "Manager"], acquire=True)
        self.manage_permission(CMFCorePermissions.View, roles=["Manager"], acquire=False)



registerType(eJSubscriptions, PROJECTNAME)
# end of class eJSubscriptions

##code-section module-footer #fill in your manual code here
##/code-section module-footer



