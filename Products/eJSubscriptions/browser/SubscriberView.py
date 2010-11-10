from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from Products.eJSubscriptions.interfaces import ISubscriberManagement
from Products.Five.browser import BrowserView

class ISubscriberView(Interface):
    """A View which provides methods to manage a subscriber.
    """
    def activate():
        """Activates a subscriber
        """

    def delete():
        """Deletes a subscriber
        """

    def disableBorder():
        """
        """    
        
class SubscriberView(BrowserView):
    """
    """    
    def activate(self):
        """
        """
        sm = ISubscriberManagement(self.context)
        sm.activate()        
        
        self._redirect(sm.status)
        
    def delete(self):
        """
        """
        utool = getToolByName(self.context, "portal_url")
        portal = utool.getPortalObject()
        
        sm = ISubscriberManagement(self.context)
        sm.delete()       

        # redirect to portal url
        message = sm.status
        portal.plone_utils.addPortalMessage(message)
        url  = portal.absolute_url()
        return self.request.response.redirect(url)
        
        self._redirect()

    def disableBorder(self):
        """
        """    
        mtool = getToolByName(self.context, "portal_membership")            
        if mtool.checkPermission("Manage portal", self.context) is None:
            self.request.set('disable_border', 1)
        
    def _redirect(self, message):
        """
        """
        # redirect
        self.context.plone_utils.addPortalMessage(message)
        url  = self.context.absolute_url()
        return self.request.response.redirect(url)
