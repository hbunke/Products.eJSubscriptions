from plone.app.registry.browser import controlpanel
from Products.eJSubscriptions.interfaces import ISubscriptionsConf

## Note: you must quickinstall plone.app.registry and z3c.form before using this!

class SubscriptionsSettingsForm(controlpanel.RegistryEditForm):
    """
    """
    schema = ISubscriptionsConf
    label = u"E-Journal Subscriptions / Notifications Settings"
    description = u"Configures ejSubscriptions"
    
    def updateFields(self):
        super(SubscriptionsSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(SubscriptionsSettingsForm, self).updateWidgets()

class SubscriptionsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SubscriptionsSettingsForm


