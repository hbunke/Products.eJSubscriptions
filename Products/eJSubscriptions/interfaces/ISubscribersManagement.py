# Zope imports
import zope

class ISubscribersManagement(zope.interface.Interface):
    """
    """
    def addSubcriber(email):
        """Add a new subscriber
        """
        
    def getSubscribers():
        """Returns all subscribers
        """    