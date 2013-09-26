from datetime import date
from zope.component import getMultiAdapter
from zope.component import getUtility
from Products.CMFCore.utils import getToolByName
from Products.AdvancedQuery import In, Eq, And, Ge
from Products.eJSubscriptions.interfaces import ISubscriptionsConf
from plone.registry.interfaces import IRegistry
# stripogram fuer paper-abstracts
from Products.stripogram import html2text


class SubscriberNotification:
    """
    Adapter for sending email alerts for new articles
    """    

    def __init__(self, context):
        """
        """
        self.context = context
        
    def mail_new_papers(self, members=False):
        """
        """ 
        
        #stool  = getToolByName(self.context, "ejsubscriptions_tool")    
        registry = getUtility(IRegistry)
        stool = registry.forInterface(ISubscriptionsConf)
       
        ejtool = getToolByName(self.context, "ejournal_tool")
        sender = "from: %s\n" % ejtool.notification_from
        
        now = date.today()
        
        if members is True:
            subscribers = self._getMembers()
            last_run = stool.last_run_member
            stool.last_run_member = now
            email = stool.changed_member_subscriptions_email
            edit_string = "/base_edit"
        else:    
            subscribers = self._getSubscribers()
            last_run = stool.last_run
            stool.last_run = now             
            email = stool.changed_subscriptions_email
            edit_string = ""            
            
        for subscriber in subscribers:
            message  = sender
            message += "to: %s\n" % subscriber.getEmail()
            message += "subject: %s\n\n" % stool.changed_subscriptions_subject
            message += email
            

            #XXX this is quick but ugly!
            if members is True:
            
                # added subscriber.getAll_jels 2007-01-10 HB
                if len(subscriber.getJel()) == 0 and subscriber.getAll_jels() == False:
                    continue
                
                if subscriber.getAll_jels() == True:
                    jels = ('A','B','C','D','E','F','G','H','I','J','K','L','M',
                        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

                else:
                    jels = subscriber.getJel()

            #XXX
            else:
                if len(subscriber.getJel()) == 0:
                    jels = ('A','B','C','D','E','F','G','H','I','J','K','L','M',
                        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
                else:
                    jels = subscriber.getJel()

            #XXX ugly block end 

            
            papers = self._getChangedPapers(jels, last_run)

            papers_txt = ""
            if len(papers) > 0:
                #XXX
                for paper in papers:
                    papers_txt += self._getTitleForMails(paper) + "\n"
                    papers_txt += paper.absolute_url() + "\n"
                    papers_txt += self._getAbstractForMails(paper) + "\n\n"
                
                #we have to use str (or bytes) here, since MailHost does not
                #handle type unicode
                message = message.encode('utf-8')
                
                message = message.replace("<changed_papers>", papers_txt)
                message = message.replace("<email>", subscriber.getEmail())                
                message = message.replace("<edit_url>", subscriber.absolute_url() + edit_string)
                message = message.replace("<delete_url>", "%s/delete" % subscriber.absolute_url())
                    
                try:
                    self.context.MailHost.send(message)
            
                except:
                    # catch and do nothing, so that the user doesn't notice an error
                    # XXX: Log error here
                    pass
            
    def _getChangedPapers(self, jel, last_run):
        """Returns all changed papers since the last run
        """

        query = And(In("portal_type", ["DiscussionPaper", "JournalPaper"]),
                    Ge("created", last_run))
                    
        papers = self.context.portal_catalog.evalAdvancedQuery(query)                
        papers = [paper.getObject() for paper in papers]

        
        # geändert 2007-12-06 HB. Alte Methode hat nur
        # komplette JELs (A14) erfasst, nicht Oberkategorien wie "A"
        result_papers = []

        for paper in papers:
          for paper_jel in paper.getJel():
            first_letter = paper_jel[0]
            if paper_jel in jel or first_letter in jel:
              result_papers.append(paper)
              break
               
        # Save papers to omit doubles
        existing_papers = {}
        for paper in result_papers:
            existing_papers[paper.getId()] = 1

        # Get JournalPaper with new Versions
        query = And(Eq("portal_type", "eJFile"),
                    Ge("created", last_run))
                    
        versions = self.context.portal_catalog.evalAdvancedQuery(query)
    
        # TODO: wie oben
        for version in versions:
            version = version.getObject()
            paper = version.aq_inner.aq_parent
            if paper.getId() not in existing_papers:
                for paper_jel in paper.getJel():  
#                    if paper_jel in jel and paper.getId():
                     first_letter = paper_jel[0]
                     if paper_jel in jel or first_letter in jel:
                        result_papers.append(paper)
                        break
                 
        return result_papers             
                
    def _getMembers(self):
        """
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type="eJMember", review_state="public")

        members = [] 
        for brain in brains:
            obj = brain.getObject()
            if obj.getAlert() == True:
                members.append(obj)
                
        return members
        
    def _getSubscribers(self):
        """
        """    
        query = And(Eq("portal_type", "eJSubscriber"),
                    Eq("review_state", "active"))
                    
        brains = self.context.portal_catalog.evalAdvancedQuery(query)
        return [brain.getObject() for brain in brains]


    def _getTitleForMails(self, paper):
        """Returns concatenated title
        moved from paperView
        """
        paper_view = getMultiAdapter((paper, paper.REQUEST), name='paperView')

        result  = paper_view.authors_as_string()
        result += "\n"
        result += paper.Title()
        result += ".("
        result += paper_view.getTitleDate()
        result += ")"
        
        return result

    
    def _getAbstractForMails(self, paper):
        """
        Returns Abstract without html
        moved from paperView
        """
        abstract = html2text(paper.getAbstract(), 
                            ignore_tags=('a','span','br','p'), 
                            indent_width=4, 
                            page_width=65)
        result = "Abstract: "
        result += abstract
        
        return result

