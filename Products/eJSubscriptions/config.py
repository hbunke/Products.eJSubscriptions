
from Products.CMFCore.permissions import setDefaultRoles

"""Common configuration constants
"""

PROJECTNAME = 'eJSubscriptions'
DEFAULT_ADD_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_PERMISSION, ('Manager', 'Owner'))

ADD_PERMISSIONS = {
       'eJSubscriber' : 'eJSubscriptions: Add Subscriber',
       'eJSubscriptions' : DEFAULT_ADD_PERMISSION,
}

product_globals = globals()
GLOBALS = globals()

