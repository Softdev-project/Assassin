#FEATURES I COULD USE
#PASSIVE UPDATING WITH INFO FROM MONOGO

import random, math
from pymongo import Connection
conn = Connection()
db = conn['1247']
killDistance = 0.005

###################
##RESTART

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
    data1 = {
        'user': "No1",
        'id': "0", 
        'lat':'lat0', #load initial coordinates
        'long':'long0', 
        'tid': 'x',
        'num_click':'0'}
    data2 = {
        'user': "No2",
        'id': "1", 
        'lat':'lat1', #load initial coordinates
        'long':'long1', 
        'tid': 'x',
        'num_click':'0'}
    switch = {'switch':'1'}
    # 0 = on
    # 1 = off
    db.usertable.insert(account1)
    db.usertable.insert(account2)
    db.datatable.insert(data1)
    db.datatable.insert(data2)
    db.idtable.insert(ids)
    db.gameon.insert(switch)

################
##SWITCH SHIT
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
        return True
    else:
        return False

####################
#USER INFO SHIT
def printUsers():
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
    

def addUser(usernamei, passwordi,):
    cres = db.usertable.find({'username':usernamei})
    res = [r for r in cres]
    n = getNewID()
    print res
    if len(res)>0:
        return False    
    nu = {'username': usernamei, 'password':passwordi, 'userid':n}
    db.usertable.save(nu)
    data = {
        'user': usernamei,
        'id': n, 
        'lat': "lat"+str(n), #load initial coordinates
        'long': "long"+str(n), 
        'tid': 'x',
        'num_click':'0'}
    db.datatable.insert (data)
    return True


def updateUser(usernamei, passwordi, passwordn):
    if validate (usernamei, passwordi):
        db.usertable.update ({'username':usernamei, 'password':passwordi}, {"$set": {'username': usernamei, 'password':passwordn}})
        return True
    return False

##############
#INGAME SHIT

def getID(username):
    cres = db.usertable.find()
    users = []
    for r in cres:
        if (r['username'] == username):
            return r['userid']
    return -1


def getName(userid):
    cres = db.usertable.find()
    users = []
    for r in cres:
        if (r['userid'] == userid):
            return r['username']
    return -1

def printData():
    cres = db.datatable.find()
    for r in cres:
        print r
        
def distance(lat1, long1, lat2, long2):
    #credit to John D. Cook
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
    # Compute spherical distance from spherical coordinates.
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc

def assignTargets():
    cres = db.datatable.find()
    users = []
    for r in cres:
        #print r
        #print r['id']
        users.append ([getName(r['id']),r['id']] )
    #assigns to next user
    l = len(users) - 1
    i = 0
    #last user
    data = {
        'user': users[l][0],
        'id': users[l][1], 
        'lat':getLat(users[l][1]), #load initial coordinates
        'long':getLong(users[l][1]), 
        'tid': users[0][1],
        'num_click':'0'}
    db.datatable.update ({'id': users[l][1]}, data)
    while (i < l) :
        data = {'user': users[i][0],
                'id': users[i][1], 
                'lat':getLat(users[i][1]), #load initial coordinates
                'long':getLong(users[i][1]), 
                'tid': users[i+1][1],
                'num_click':'0'}
        db.datatable.update ({'id': users[i][1]}, data)
        i = i + 1

def checkStatus(userid):
    cres = db.datatable.find()
    for r in cres:
        if (r['id'] == userid):  
            return True
    return False    

def getTargetID(userid):
    cres = db.datatable.find()
    for r in cres:
        if (r['id'] == userid): 
            return r['tid']
    return -1

def getLat (tid):
    cres = db.datatable.find()
    for r in cres:
        if (r['id'] == tid):
            return r['lat']
    return 0

def getLong (tid): 
    cres = db.datatable.find()
    for r in cres:
        if (r['id'] == tid):
            return r['long']
    return 0

def updateLat (uid, lat):
    cres = db.datatable.find()
    for r in cres:
        if (r['id'] == uid):
            data = {'lat':lat}
            db.datatable.update ({'id':uid}, {"$set": data})

def updateLong (uid, long):
    cres = db.datatable.find()
    for r in cres:
        if (r['id'] == uid):
            data = {'long':long}
            db.datatable.update ({'id':uid}, {"$set": data})



def killCheck(lat1, long1, lat2, long2):
    return (distance (long1, long2) < killDistance)

def kill(userid):
    cres = db.datatable.find({'id':userid})
    for r in cres:
        db.datatable.remove({'id':userid})
    #assignTargets()


restart()
addUser ("No3", "number3")
addUser ("No4", "number4")
print "Users"
printUsers()
print "Test get ID"
print getID("No3")
print "Test get Name"
print getName("0")
print "Data"
printData()
print "Lat"
print getLat("1")
print"Assign targets"
assignTargets()
print"Data"
printData()
kill('0')
print "Test Kill"
assignTargets()
printData()
print "check status"
print checkStatus ("0")
print checkStatus ("1")
print checkStatus ("2")
print checkStatus ("3")
print "update lat"
updateLat ("1", "1lat")
printData()
