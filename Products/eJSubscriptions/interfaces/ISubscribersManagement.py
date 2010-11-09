# Zope imports
import zope

class ISubscribersManagement(zope.interface.Interface):
    """
    """
    def addSubscriber(email):
        """Add a new subscriber
        """
        
    def getSubscribers():
        """Returns all subscribers
        """    
