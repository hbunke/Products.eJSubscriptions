# Zope imports 
import zope                                                              
from zope.interface import Interface

# CMF imports
from Products.CMFCore.utils import getToolByName

# Five imports
from Products.Five.browser import BrowserView

class IConfigletView(Interface):
    """
    """
    def edit():
        """
        """

    def getFieldValue():
        """
        """
        
class ConfigletView(BrowserView):
    """
    """    
    def edit(self):
        """
        """        
        # remove value of button which is passed with field values
        del self.request.form["ejsubscriptions_edit_configlet"]        

        # XXX Dangerous?
        ejtool = getToolByName(self.context, "ejsubscriptions_tool")
        ejtool.manage_changeProperties(self.request.form)
        
        url  = "%s/ejsubscriptions_configlet_form" % self.context.absolute_url()
        url += "?portal_status_message=%s" % "Your changes have been saved."
        self.request.response.redirect(url)

    def getFieldValue(self, field):
        """
        """
        ejtool = getToolByName(self.context, "ejsubscriptions_tool")        
        value = ejtool.getProperty(field, '')
        
        # Change value of the tool's line fields in string
        if isinstance(value, (list, tuple)):
            value = "\n".join(value)
 
        return value
            