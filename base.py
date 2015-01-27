#FEATURES I COULD USE
#PASSIVE UPDATING WITH INFO FROM MONOGO
import random, math
from pymongo import Connection
conn = Connection()
db = conn['1247']
killDistance = 0.005

def restart():
    ##need counter for id
    db.usertable.drop()
    db.datatable.drop()
    db.idtable.drop()
    db.gameon.drop()
    ids = {'idnum':'2'}
    account1 = {'username': 'No1',
                'userid': '0',
                'password':'number1',}
    account2 = {'username': 'No2',
                'userid': '1',
                'password':'number2',}
    data = {'user':'user',
    'uid':'0', 
    'ulat':'0', 
    'ulong':'0', 
    'target':'target',
    'tid':'1',
    'tlat':'0',
    'tlong':'0',
    'num_click':'0',
    'status':'alive'}
    switch = {'switch':'1'}
    db.usertable.insert(account1)
    db.usertable.insert(account2)
    db.datatable.insert(data)
    db.idtable.insert(ids)
    db.gameon.insert(switch)

def printUsers():
    cres = db.usertable.find()
    #{}, {'_id':False})
    #print cres
    #res = [r
    for r in cres:
        print r

def printData():
    cres = db.datatable.find()
    #{}, {'_id':False})
    #print cres
    #res = [r
    for r in cres:
        print r

def gameON():
    cres = db.gameon.find()
    n = int(cres[0]['switch'])
    if (n == 0):
        db.gameon.update ({'switch':'0'}, {'$set':{'switch':"1"}})
        return False
    else:
        db.gameon.update ({'switch':'1'}, {'$set':{'switch':"0"}})
        return True

def gameONcheck():
    cres = db.gameon.find()
    n = int(cres[0]['switch'])
    if (n == 0):
        return False
    else:
        return True


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


def addUser(usernamei, passwordi,):
    cres = db.usertable.find({'username':usernamei})
    res = [r for r in cres]
    print res
    if len(res)>0:
        return False    
    nu = {'username': usernamei, 'password':passwordi, 'userid':getNewID()}
    db.usertable.save(nu)
    return True


def updateUser(usernamei, passwordi, passwordn):
    if validate (usernamei, passwordi):
        db.usertable.update ({'username':usernamei, 'password':passwordi}, {"$set": {'username': usernamei, 'password':passwordn}})
        return True
    return False



def assignTargets():
    #test this out first
    cres = db.usertable.find()
    users = []
    for r in cres:
        users.append ([r['username'],r['userid']] )
    #assigns to next user
    l = len(users) - 1
    i = 0
    #last user
    data = {'user': users[l][0],
    'uid': users[l][1], 
    'ulat':'0', #load initial coordinates
    'ulong':'0', 
    'target': users[0][0],
    'tid': users[0][1],
    'tlat':'0',
    'tlong':'0',
    'num_click':'0',
    'status':'alive'}
    db.datatable.insert (data)
    while (i < l) :
        data = {'user': users[i][0],
                'uid': users[i][1], 
                'ulat':'0', #load initial coordinates
                'ulong':'0', 
                'target': users[i+1][0],
                'tid': users[i+1][1],
                'tlat':'0',
                'tlong':'0',
                'num_click':'0',
                'status':'alive'}
        db.datatable.insert (data)
        i = i + 1

def killStatus(id):
    cres = db.usertable.find({'userid':str(id)})
    for r in cres:
        db.usertable.drop#something
    reassignTargets()#upsert?
    
def distance (a, b):
    b = b-a
    return math.sqrt ((a*a)+(b*b))

def kill(lat1, long1, lat2, long2):
    return ((distance (lat1, lat2) < killDistance) and (distance (long1, long2) < killDistance))

restart()
print gameON()
