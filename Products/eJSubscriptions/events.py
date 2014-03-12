import zope

# CMFCore imports
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from Products.eJSubscriptions.interfaces import ISubscriptionsConf
from plone.registry.interfaces import IRegistry

from Products.eJournal import settings


class ISubscriberAdded(zope.interface.Interface):
    """A marker interface for the event: subscriber has been added.
    """
    object = zope.interface.Attribute("Object")    

class SubscriberAdded(object):
    """An Event, which is triggered when a subscriber has been added.
    """
    zope.interface.implements(ISubscriberAdded)
    
    def __init__(self, object):
        self.object = object        


class ISubscriberActivated(zope.interface.Interface):
    """A marker interface for the event: subscriber has been activated.
    """
    object = zope.interface.Attribute("Object")    
    
class SubscriberActivated(object):
    """An Event, which is triggered when a subscriber has been activated
    """
    zope.interface.implements(ISubscriberActivated)
    
    def __init__(self, object):
        self.object = object      
                
# Subscribers        

def sendAddedMail(event):
    """
    """
    object = event.object

    registry = getUtility(IRegistry)
    stool = registry.forInterface(ISubscriptionsConf)

    #XXX Beware when moving ejtool to utility!!!
    ejtool = getToolByName(object, "ejournal_tool")    
    
    message = stool.added_subscriber_email.encode('utf-8')
    message = message.replace("<email>", object.getEmail())
    message = message.replace("<activate_url>", "%s/activate" % object.absolute_url())
        
    header  = "From: %s\n" % settings.notification_from
    header += "To: %s\n"  % object.getEmail()
    header += "Subject: %s\n" % stool.added_subscriber_subject.encode('utf-8')
    header += "Content-Type: text/plain; charset=utf-8\n\n"

    mailtext = header+message
    #import pdb; pdb.set_trace()
    object.MailHost.send(mailtext)
   

def sendActivatedMail(event):
    """
    """
    object = event.object

    registry = getUtility(IRegistry)
    stool = registry.forInterface(ISubscriptionsConf)

    ejtool = getToolByName(object, "ejournal_tool")    
    
    message = stool.activated_subscriber_email.encode('utf-8')
    
    message = message.replace("<email>", object.getEmail())
    message = message.replace("<edit_url>", object.absolute_url())
    message = message.replace("<delete_url>", "%s/delete" % object.absolute_url())
    
    header  = "from: %s\n" % settings.notification_from
    header += "to: %s\n"  % object.getEmail()
    header += "subject: %s\n" %  stool.activated_subscriber_subject.encode('utf-8')
    header += "Content-Type: text/plain; charset=utf-8\n\n"
    message = header + message
    
    object.MailHost.send(message)
