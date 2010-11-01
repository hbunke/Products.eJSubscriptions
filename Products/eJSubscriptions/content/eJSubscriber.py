# -*- coding: utf-8 -*-
#
# File: eJSubscriber.py
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
from Products.eJSubscriptions.interfaces.IeJSubscriber import IeJSubscriber
from Products.eJSubscriptions.config import *

##code-section module-header #fill in your manual code here
from Products.AutocompleteWidget.AutocompleteWidget import AutocompleteWidget
from Products.CMFCore.utils import getToolByName
##/code-section module-header

schema = Schema((

    LinesField(
        name='jel',
        widget=AutocompleteWidget
        (
            label=' E-mail alert on new papers on the following JEL classifications',
            label_msgid='eJSubscriptions_label_jel',
            i18n_domain='eJournal',
        ),
        enforceVocabulary=1,
        vocabulary="_getJEL"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

eJSubscriber_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
eJSubscriber_schema["title"].widget.label = "E-Mail"
eJSubscriber_schema["title"].write_permission = "Manage portal"
##/code-section after-schema

class eJSubscriber(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IeJSubscriber)

    # This name appears in the 'add' box
    archetype_name = 'eJSubscriber'

    meta_type = 'eJSubscriber'
    portal_type = 'eJSubscriber'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'eJSubscriber.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "eJSubscriber"
    typeDescMsgId = 'description_edit_ejsubscriber'

    _at_rename_after_creation = True

    schema = eJSubscriber_schema

    ##code-section class-header #fill in your manual code here
    aliases = ({'(Default)' : 'ejsubscriber_edit',
                'view'      : 'ejsubscriber_edit',
                'base_view' : 'ejsubscriber_edit',
                'edit'      : 'ejsubscriber_edit',
                'base_edit' : 'ejsubscriber_edit',
                })
    ##/code-section class-header

    # Methods

    # Manually created methods

    def setEmail(self, value):
        """
        """
        self.getField("title").set(self, value)

    def getEmail(self):
        """
        """
        return self.getField("title").get(self)

    def _getJEL(self):
        """
        """
        ejtool = getToolByName(self, "ejournal_tool")
        return ejtool.getJELShort()

    def setJel(self, value):
        """Overwritten to sort JEL classes.

           Why? By using AutocompleteWidget the user is free to select JEL
           classes in any order.
        """
        value = list(value)
        value.sort()
        self.getField('jel').set(self, value)

registerType(eJSubscriber, PROJECTNAME)
# end of class eJSubscriber

##code-section module-footer #fill in your manual code here
##/code-section module-footer



