# Zope imports
from zope.interface import implements
from zope.event import notify

# Validation imports
from Products.validation.validators.BaseValidators import EMAIL_RE
        
# CMF imports
from Products.CMFCore.utils import getToolByName

# eJSubscriptions imports
from Products.eJSubscriptions.interfaces import ISubscriberManagement
from Products.eJSubscriptions.config import ALREADY_ACTIVATED, ACTIVATED, DELETED
from Products.eJSubscriptions.events import SubscriberActivated

class SubscriberManager:
    """Adapter which manages states of a subscriber
    """    
    implements(ISubscriberManagement)

    def __init__(self, context):
        """
        """
        self.context = context
        self.status = ""

    def activate(self):
        """Activates a subscriber 
        """
        wftool = getToolByName(self.context, "portal_workflow")

        review_state = wftool.getInfoFor(self.context, "review_state")
        if review_state == "waiting":
            wftool.doActionFor(self.context, "activate")
            # send activated event
            notify(SubscriberActivated(self.context))
            self.status = ACTIVATED                        
        elif review_state == "active":
            self.status = ALREADY_ACTIVATED            
                    
    def delete(self):
        """Deletes a subscriber
        """
        self.status = DELETED
        parent = self.context.aq_inner.aq_parent
        parent._delObject(self.context.id)
                
