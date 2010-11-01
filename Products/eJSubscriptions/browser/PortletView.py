# python imports
from urllib import quote

# Zope imports 
import zope                                                              
from zope.interface import Interface
        
# CMF imports
from Products.CMFCore.utils import getToolByName

# eJSubscriptions
from Products.eJSubscriptions.interfaces import ISubscribersManagement

# Five imports
from Products.Five.browser import BrowserView


class IPortletView(Interface):
    """Interface, which provides methods for the portlet.
    """
    def addSubscriber():
        """
        """
        
class PortletView(BrowserView):
    """
    """    
    def addSubscriber(self):
        """
        """
        stool = getToolByName(self.context, "ejsubscriptions_tool")
        folder = stool.path_to_subscriptions
        
        # data
        email = self.request.get("email", "")
        folder = self.context.restrictedTraverse(folder)

        # add
        sm = ISubscribersManagement(folder)        
        sm.addSubscriber(email)

        # redirect
        message = sm.status_message

        self.context.plone_utils.addPortalMessage(message)
        url  = self.context.absolute_url()
        self.request.response.redirect(url)
