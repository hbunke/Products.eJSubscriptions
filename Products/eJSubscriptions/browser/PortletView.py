from zope.interface import Interface, implements
#from Products.CMFCore.utils import getToolByName
from Products.eJSubscriptions.interfaces import ISubscribersManagement
from Products.Five.browser import BrowserView
from zope.component import getUtility
from Products.eJSubscriptions.interfaces import ISubscriptionsConf
from plone.registry.interfaces import IRegistry
from zope.component.hooks import getSite


class IPortletView(Interface):
    """Interface, which provides methods for the portlet.
    """
    def add_subscriber():
        """
        """
        
class PortletView(BrowserView):
    """
    """  
    implements(IPortletView)

    def add_subscriber(self):
        """
        """
        #stool = getToolByName(self.context, "ejsubscriptions_tool")
        registry = getUtility(IRegistry)
        stool = registry.forInterface(ISubscriptionsConf)
        
        #hardcoding the subscriptions folder
        portal = getSite()
        if not portal.subscriptions:
            portal.invokeFactory(id="subscriptions",
                type_name="eJSubscriptions")
        folder = portal.subscriptions

        #folder = stool.path_to_subscriptions
        
        # data
        email = self.request.get("email", "")
        
        #folder = self.context.restrictedTraverse(folder)

        # add
        sm = ISubscribersManagement(folder)        
        sm.addSubscriber(email)

        # redirect
        message = sm.status_message

        self.context.plone_utils.addPortalMessage(message)
        url  = self.context.absolute_url()
        self.request.response.redirect(url)
