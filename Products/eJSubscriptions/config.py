from Products.CMFCore.permissions import setDefaultRoles


PROJECTNAME = 'eJSubscriptions'
DEFAULT_ADD_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_PERMISSION, ('Manager', 'Owner'))

ADD_PERMISSIONS = {
       'eJSubscriber' : 'eJSubscriptions: Add Subscriber',
       'eJSubscriptions' : DEFAULT_ADD_PERMISSION,
}

product_globals = globals()
GLOBALS = globals()

# Texte
VALID              = "Your e-mail has been added. Shortly you will get an activation e-mail. Please follow its instructions to activate your subscription."
NOT_VALID          = "Sorry, this is not a valid e-mail address."
ALREADY_REGISTERED = "Your e-mail address has already been registered."

ACTIVATED          = "Your e-mail address has been activated"
ALREADY_ACTIVATED  = "Your e-mail address has already been activated"
DELETED            = "Your e-mail address has been deleted"

