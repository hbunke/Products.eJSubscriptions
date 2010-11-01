# Zope imports
import zope

# CMFCore imports
from Products.CMFCore.utils import getToolByName

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

    stool = getToolByName(object, "ejsubscriptions_tool")
    ejtool = getToolByName(object, "ejournal_tool")    
    
    message = stool.added_subscriber_email

    message = message.replace("<email>", object.getEmail())
    message = message.replace("<activate_url>", "%s/activate" % object.absolute_url())
        
    header  = "from: %s\n" % ejtool.notification_from
    header += "to: %s\n"  % object.getEmail()
    header += "subject: %s\n\n" % stool.added_subscriber_subject
    message = header + message
    
    try:
        # Need context of object here to find MailHost
        object.MailHost.send(message)
    except:
        # catch and do nothing, so that the user doesn't notice an error
        pass

def sendActivatedMail(event):
    """
    """
    object = event.object

    stool = getToolByName(object, "ejsubscriptions_tool")
    ejtool = getToolByName(object, "ejournal_tool")
         
    message = stool.activated_subscriber_email
    
    message = message.replace("<email>", object.getEmail())
    message = message.replace("<edit_url>", object.absolute_url())
    message = message.replace("<delete_url>", "%s/delete" % object.absolute_url())
    
    header  = "from: %s\n" % ejtool.notification_from
    header += "to: %s\n"  % object.getEmail()
    header += "subject: %s\n\n" % stool.activated_subscriber_subject
    message = header + message
    
    try:
        # Need context of object here to find MailHost
        object.MailHost.send(message)
    except:
        # catch and do nothing, so that the user doesn't notice an error
        pass
