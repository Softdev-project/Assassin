import random
from pymongo import Connection

conn = Connection()

db = conn['1247']


def restart():
    ##need counter for id
    db.usertable.drop()
    accounts = {'username': 'testing', 'password':'testing'}
    data = {'user': 'user', 
    'uid':'00000', 
    'ulat':'0', 
    'ulong':'0', 
    'target':'target'
    'tid':'00001',
    'tlat':'0',
    'tlong':'0'
    'num_click':'0'}
    db.usertable.insert(tdic)   

def printData():
    cres = db.usertable.find()
    #{}, {'_id':False})
    #print cres
    #res = [r
    for r in cres:
        print r

def validate(usernamei, passwordi):
    cres = db.usertable.find({'username': usernamei,'password':passwordi})
    res = [r for r in cres]  
    if len(res)>0:
        return True
    return False

#def validate(usernamei, passwordi):
#    def decorate(func):
#        def inner(*args):
#            cres = db.usertable.find({'username': usernamei,'password': passwordi})
#            res = [r for r in cres]  
#            if len(res)>0:
#                return func(args, kwargs)
#            
#            error = "Invalid credentials"
#            return render_template ("login.html", error = error)
#        return inner

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
    
