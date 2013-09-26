# -*- coding: utf-8 -*-

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
import zope
from Products.ATContentTypes.content.folder import ATFolder
from Products.eJSubscriptions.interfaces import IeJSubscriptions
from Products.eJSubscriptions.config import *
from Products.CMFCore import permissions as CMFCorePermissions


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



