from Products.Five.browser import BrowserView
from Products.eJSubscriptions.interfaces import ISubscriberNotification


class View(BrowserView):
    """
    sending email alerts
    """

    def mail_member_subscriptions(self):
        """
        """
        sm = ISubscriberNotification(self.context)
        sm.mail_new_papers(members=True)

    def mail_subscriptions(self):
        """
        """
        sm = ISubscriberNotification(self.context)
        sm.mail_new_papers(members=False)
