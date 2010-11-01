#from Products.CMFCore.CMFCorePermissions import ManagePortal
from Products.CMFCore.utils import getToolByName
from Products.eJSubscriptions.workflows import ejsubscriber_workflow

configlets = \
( { 'id'         : 'ejsubscriptions'
  , 'name'       : 'eJSubscriptions'
  , 'action'     : 'string:${portal_url}/ejsubscriptions_configlet_form' 
  , 'category'   : 'Products'
  , 'appId'      : 'eJSubscriptions'
  , 'permission' :  'cmf.ManagePortal'
  , 'imageUrl'   : 'tool.gif'
  }
,
)        

def install(self):
    # install tool
    portal = getToolByName(self, 'portal_url').getPortalObject()
    if not hasattr(self, 'ejsubscriptions_tool'):
        portal.manage_addProduct['eJSubscriptions'].manage_addTool(type="eJSubscriptions Tool")

    # add configlet
    configTool = getToolByName(self, 'portal_controlpanel', None)
    if configTool:
        lets = [c['id'] for c in configTool.enumConfiglets(group='Plone')]
        for conf in configlets:
            if conf['id'] not in lets:
                configTool.registerConfiglet(**conf)

    ## install workflow
    wf_tool = getToolByName(self, 'portal_workflow')    

    if not 'ejsubscriptions_workflow' in wf_tool.objectIds():
         wf_tool.manage_addWorkflow('ejsubscriber_workflow (eJSubscriber Workflow)',
                                    'ejsubscriber_workflow')

    wf_tool.setChainForPortalTypes(('eJSubscriber',), chain='ejsubscriber_workflow')    
    wf_tool.setChainForPortalTypes(('eJSubscriptions',), chain='')
    wf_tool.updateRoleMappings()

def uninstall(self):
    configTool = getToolByName(self, 'portal_controlpanel', None)
    if configTool:
        for conf in configlets:
            configTool.unregisterConfiglet(conf['id'])        
