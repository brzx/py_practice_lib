# demonstration of using the BeatBox library to call the sforce API

import os
import sys
import beatbox
import datetime

import beatbox
svc = beatbox.PythonClient()
beatbox.gzipRequest = False
svc.serverUrl = svc.serverUrl.replace('login.', 'test.')
ls = svc.login('sfdc username', 'pw')

dr = svc.describeSObjects(sobjectName)
a = dr[0] 

object_name=a.name
object_label=a.label
object_fields = a.fields

dg = svc.describeGlobal()
types = dg['types']

object_list = dg['sobjects']
for t in object_list:
    t.name
    t.label
    t.labelPlural
    

class BeatBoxDemo(object):
    def login(self):
        loginResult = svc.login('sfdc username', 'pw')
        print("sid = " + str(loginResult[sf.sessionId[1]]))
        print("welcome " + str(loginResult[sf.userInfo[1]][sf.userFullName[1]]))

    def getServerTimestamp(self):
        print("\ngetServerTimestamp " + svc.getServerTimestamp())

    def describeGlobal(self):
        print("\ndescribeGlobal")
        dg = svc.describeGlobal()
        for t in dg[sf.sobjects:]:
            print(str(t[sf.name[1]]) + " \t " + str(t[sf.label[1]]))

    def describeTabs(self):
        print("\ndescribeTabs")
        dt = svc.describeTabs()
        for t in dt:
            print(str(t[sf.label[1]]))

    def describeSearchScopeOrder(self):
        print("\ndescribeSearchScopeOrder")
        types = svc.describeSearchScopeOrder()
        for t in types:
            print("\t" + str(t[sf.name[1]]) + " : " + str(t[sf.keyPrefix[1]]))

    def dumpQueryResult(self, qr):
        print("query size = " + str(qr[sf.size[1]]))

        for rec in qr[sf.records:]:
            print(str(rec[0]) + " : " + str(rec[2]) + " : " + str(rec[3]))

        if (str(qr[sf.done]) == 'false'):
            print("\nqueryMore")
            qr = svc.queryMore(str(qr[sf.queryLocator[1]]))
            for rec in qr[sf.records[1]:]:
                print(str(rec[0]) + " : " + str(rec[2]) + " : " + str(rec[3]))

    # sObjects methods
    # special

    def getUserInfo(self):
        print("\ngetUserInfo")
        ui = svc.getUserInfo()
        print("hello " + str(ui[sf.userFullName[1]]) + " from " + str(ui[sf.organizationName[1]]))

    def resetPassword(self):
        ui = svc.getUserInfo()
        print("\nresetPassword")
        pr = svc.resetPassword(str(ui[sf.userId[1]]))
        print("password reset to " + str(pr[sf.password[1]]))

        print("\nsetPassword")
        svc.setPassword(str(ui[sf.userId[1]]), self.password)
        print("password set back to original password")

    def convertLead(self):
        print("\nconvertLead")
        lead = {'type': 'Lead',
                'LastName': 'Fell',
                'Company': '@superfell'}
        leadId = str(svc.create(lead)[sf.id[1]])
        print("created new lead with id " + leadId)
        convert = {'leadId': leadId,
                   'convertedStatus': 'Closed - Converted',
                   'doNotCreateOpportunity': 'true'}
        res = svc.convertLead(convert)
        print("converted lead to contact with Id " + str(res[sf.contactId[1]]))

    def describeSObjects(self):
        print("\ndescribeSObjects(Account)")
        desc = svc.describeSObjects("Account")
        for f in desc[sf.fields:]:
            print("\t" + str(f[sf.name]))

        print("\ndescribeSObjects(Lead, Contact)")
        desc = svc.describeSObjects(["Lead", "Contact"])
        for d in desc:
            print(str(d[sf.name]) + "\n" + ("-" * len(str(d[sf.name]))))
            for f in d[sf.fields:]:
                print("\t" + str(f[sf.name]))

    def describeLayout(self):
        print("\ndescribeLayout(Account)")
        desc = svc.describeLayout("Account")
        for layout in desc[sf.layouts:]:
            print("sections in detail layout " + str(layout[sf.id]))
            for s in layout[sf.detailLayoutSections:]:
                print("\t" + str(s[sf.heading]))


if __name__ == "__main__":
    demo = BeatBoxDemo()
    demo.login()
    demo.getServerTimestamp()
    demo.getUserInfo()
    #demo.convertLead()
    # demo.resetPassword()
    '''demo.describeGlobal()
    demo.describeSearchScopeOrder()
    demo.describeTabs()
    demo.describeSObjects()
    demo.describeLayout()
    demo.query()
    demo.upsert()
    demo.create()
    demo.update()
    demo.getUpdated()
    demo.delete()
    demo.getDeleted()
    demo.queryAll()
    demo.undelete()
    demo.retrieve()
    demo.retrieve_by_iterclient()
    demo.search()'''
