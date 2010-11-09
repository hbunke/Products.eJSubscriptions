# -*- coding: utf-8 -*-
# Dr. Hendrik Bunke, h.bunke@zbw.eu

from zope.interface import Interface, Attribute
from zope import schema

class ISubscriptionsConf(Interface):
    """configuration utility for eJSubscriptions. Replaces the oldstyle tool.
    Uses plone.registry
    """
    
    path_to_subscriptions = schema.TextLine(
            title = u"Path To Subscriptions",
            description = u"Folder within subscribers are created.",
            required = True,
            )

    added_subscriber_subject = schema.TextLine(
            title = u'Added Subscriber Subject',
            description = u'Will be used as subject for the added subscriber mail',
            required = True,
            )

    added_subscriber_email = schema.Text(
            title = u'Added Subscriber E-Mail',
            description = u'Will be used as text for the added subscriber mail.',
            required = True,
            )

    activated_subscriber_subject = schema.TextLine(
            title = u'Activated Subscriber Subject',
            description = u'Will be used as subject for the activated subscriber mail.',
            required = True,
            )
    
    activated_subscriber_email = schema.Text(
            title = u'Activated Subscriber E-Mail',
            description = u'Will be used as text for the activated subscriber mail.',
            required = True,
            )

    changed_subscriptions_subject = schema.TextLine(
            title = u'Changed Papers Notification for Anonymous Subscribers Subject',
            description = u'Will be used as subject for changed subscriptions mail for anonymous subscribers.',
            required = True,
            )

    changed_subscriptions_email = schema.Text(
            title =u'Changed Papers Notification for Anonymous Subscribers E-Mail',
            description = u'Will be used as subject for changed subscriptions mail for anonymous subscribers.',
            required = True,
            )

    changed_member_subscriptions_subject = schema.TextLine(
            title= u'Changed Papers Notification for Registered Subscribers Subject',
            description =  u'Will be used as subject for changed subscriptions mail for registered subscribers',
            required = True, 
            )
  
    
    changed_member_subscriptions_email = schema.Text(
        title = u'Changed Papers Notification For Registered Subscribers',
        description = u'Will be used as text for changed subscriptions mail for registered subscribers',
        required = True,
        )

    last_run = schema.Date(
            title = u'Last Run for Anonymous',
            required = False,
            )

    last_run_member = schema.Date(
            title = u'Last Run for Members',
            required = False,
            )
            
