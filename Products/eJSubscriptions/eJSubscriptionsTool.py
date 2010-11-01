# Zope imports
from Globals import InitializeClass
from OFS.Folder import Folder 
from AccessControl import ClassSecurityInfo

# Archetypes imports
from Products.Archetypes.atapi import *

# CMFCore imports
from Products.CMFCore.utils import UniqueObject   
from Products.CMFCore.utils import getToolByName

class eJSubscriptionsTool(UniqueObject, Folder):
    """A tool to administrate sidewide eJSubscriptions Tool
    """
    id = 'ejsubscriptions_tool'
    meta_type= 'eJSubscriptions Tool'

    security = ClassSecurityInfo()

    _properties=({'id':'path_to_subscriptions', 'type': 'string', 'mode': 'w'},
                 {'id':'added_subscriber_email', 'type': 'text', 'mode': 'w'},
                 {'id':'added_subscriber_subject', 'type': 'string', 'mode': 'w'},
                 {'id':'activated_subscriber_email', 'type': 'text', 'mode': 'w'},
                 {'id':'activated_subscriber_subject', 'type': 'string', 'mode': 'w'},
                 {'id':'changed_subscriptions_email', 'type': 'text', 'mode': 'w'},
                 {'id':'changed_subscriptions_subject', 'type': 'string', 'mode': 'w'},                 
                 {'id':'changed_member_subscriptions_email', 'type': 'text', 'mode': 'w'},
                 {'id':'changed_member_subscriptions_subject', 'type': 'string', 'mode': 'w'},                                  
                 {'id':'last_run', 'type': 'date', 'mode': 'w'},
                 {'id':'last_run_member', 'type': 'date', 'mode': 'w'},                 
                 )
    
    def __init__(self, id=None):
        self.path_to_subscriptions = ""
        self.added_subscriber_email = ""
        self.added_subscriber_subject = ""        
        self.activated_subscriber_email = ""
        self.activated_subscriber_subject = ""
        self.changed_subscriptions_email = ""
        self.changed_subscriptions_subject = ""
        self.changed_member_subscriptions_email = ""
        self.changed_member_subscriptions_subject = ""        
        self.last_run = ""
        self.last_run_member = ""        

                              
InitializeClass(eJSubscriptionsTool)
