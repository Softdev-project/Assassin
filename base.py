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
    data = {'user':'user',
    'uid':'0', 
    'ulat':'0', 
    'ulong':'0', 
    'tid':'1',
    'num_click':'0'}
    switch = {'switch':'1'}
    # 0 = on
    # 1 = off
    db.usertable.insert(account1)
    db.usertable.insert(account2)
    db.datatable.insert(data)
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
        return False
    else:
        return True

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

##############
#INGAME SHIT

def printData():
    cres = db.datatable.find()
    #{}, {'_id':False})
    #print cres
    #res = [r
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
    'tid': users[0][1],
    'num_click':'0'}
    db.datatable.insert (data)
    while (i < l) :
        data = {'user': users[i][0],
                'uid': users[i][1], 
                'ulat':'0', #load initial coordinates
                'ulong':'0', 
                'tid': users[i+1][1],
                'tlong':'0'}
        db.datatable.insert (data)
        i = i + 1
    
 
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

def checkStatus(userid):
    cres = db.usertable.find()
    users = []
    for r in cres:
        if (r['userid'] == userid): 
            return True
        return False
    return False    


def killCheck(lat1, long1, lat2, long2):
    return (distance (long1, long2) < killDistance)

def kill(userid):
    cres = db.usertable.find({'userid':userid})
    for r in cres:
        db.usertable.drop#something
    reassignTargets()#upsert?



restart()
print gameON()
