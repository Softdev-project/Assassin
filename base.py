import random
from pymongo import Connection

conn = Connection()

db = conn['1247']


def restart():
    ##need counter for id
    db.usertable.drop()
    db.datatable.drop()
    db.idtable.drop()
    ids = {'idnum':'2'}
    accounts = {'username': 'test',
                'userid': '0',
                'password':'test'}
    data = {'uid':'0', 
    'ulat':'0', 
    'ulong':'0', 
    'target':'target',
    'tid':'1',
    'tlat':'0',
    'tlong':'0',
    'num_click':'0'}
    db.usertable.insert(accounts)
    db.datatable.insert(data)
    db.idtable.insert(ids)

def printData():
    cres = db.usertable.find()
    #{}, {'_id':False})
    #print cres
    #res = [r
    for r in cres:
        print r

def updateID():
    i = db.idtable.find()
    num = 0;
    for n in i:
        #num = int(n) + 1
        num = int(n['idnum']) + 1
        db.idtable.update ({'idnum':n['idnum']}, {"$set": {'idnum': str(num)}})
        print n['idnum']
    #print num

def getNewID():
    i = db.idtable.find()
    num = "";
    for n in i:
        num = n['idnum']
    updateID()
    return num

def validate(usernamei, passwordi):
    cres = db.usertable.find({'username': usernamei,'password':passwordi})
    res = [r for r in cres]  
    if len(res)>0:
        return True
    return False



def addUser(usernamei, passwordi):
    cres = db.usertable.find({'username':usernamei})
    res = [r for r in cres]
    print res
    if len(res)>0:
        return False    
    nu = {'username': usernamei, 'password':passwordi}
    db.usertable.save(nu)
    return True


def updateUser(usernamei, passwordi, passwordn):
    if validate (usernamei, passwordi):
        db.usertable.update ({'username':usernamei, 'password':passwordi}, {"$set": {'username': usernamei, 'password':passwordn}})
        return True
    return False
    
restart()
