# Python imports
import re
import random

# Zope imports
from zope.interface import implements
from zope.event import notify

# Validation imports
from Products.validation.validators.BaseValidators import EMAIL_RE
        
# CMF imports
from Products.CMFCore.utils import getToolByName

# eJournal imports
from Products.eJSubscriptions.interfaces import ISubscribersManagement
from Products.eJSubscriptions.AppConfig import VALID, NOT_VALID, ALREADY_REGISTERED
from Products.eJSubscriptions.events import SubscriberAdded

class SubscribersManager:
    """Adapter which manages related objects.
    """    
    implements(ISubscribersManagement)

    def __init__(self, context):
        """
        """
        self.context = context
        self.status_message = VALID
        
    def addSubscriber(self, email):
        """Adds a subscriber
        """        
        # check
        if self._isValid(email) == False:
            self.status_message = NOT_VALID
            return False

        # Normalize E-Mail
        email = email.lower()

        if self._isAlreadyRegistered(email) == True:
            self.status_message = ALREADY_REGISTERED
            return False

        # Add Subscriber
        new_id = self._generateUniqueId()
        self.context.invokeFactory(id=new_id, type_name="eJSubscriber")
        subscriber = getattr(self.context, new_id)
        subscriber.setEmail(email)
        subscriber.reindexObject()        

        # send added event
        notify(SubscriberAdded(subscriber))
               
        return True
        
    def getSubscribers(self):
        """
        """        
        return [s.getEmail() for s in self.context.objectValues("eJSubscriber")]
    
    
    # Privates   
    def _isValid(self, email):
        """
        """
        mo = re.search(EMAIL_RE, email)
                
        if mo is None:
            return False
        
        return True
            
    def _isAlreadyRegistered(self, email):
        """
        """    
        if email in self.getSubscribers():
            return True
        return False

    def _generateUniqueId(self):
        """
        """
        random.seed()        
        code = "".join([str(random.randint(0,9)) for i in range(0,20)])                           
        return code