## Anathema Web App
========
### Assassin
--------
project: <strike>http://help.wtf.im:1247</strike>
 <strike>http://104.236.107.63:1247/ </strike> links are unavailable

video: https://vimeo.com/118027405


-----
Leader: Jessica Ng

Members: Jason Lu, Nathaniel Brassell, Vanessa Yan

Jessica
* Accounts
* Mongodb
* Flask

Jason
* Nginx
* Server
* Mongo/JavaScript/Ajax connection

Nathaniel
* Nginx
* Server
* Mongo/Javascript/Ajax connection
* Gunicorn

Vanessa
* Mapping
* Flask
* CSS

Wish List
---------
* Auto updating geolocation
* No port number on website

Bugs
----
* Possible problems with too many games/people
* Geolocation accracy can vary, leading to discrepanceies in calculating distance. 
 * Can improve accuracing by 'sending more data'

Changelog
---------
V5.0 (1/28)
* Full operating site

V4.0 (1/20)
* Skeleton HTML site is on the html branch
* Pull request for mapping to html

V3.0 (1/16)
* site shows map ON DROPLET WHOOO
* also port 8888 is running a flask app fucking yes
* still need to remove port ref but blehhh

v2.0 (1/8)
* made site to show map with Google API but not on droplet yet. 

v1.1 (1/7)
* Domain registered & added nginx to box
* http://help.wtf.im/

v1.0 (1/6)
* First droplet deleted, new one made.

v0.0-1 (1/5)
* Server no bueno no mo' (we were apparently waging war against other servers)
* submitted a ticket. no responce

v0.01 (12/22)
* Server is up! Runs at http://104.236.107.63:8000/

v0.0 (12/18)
* made repo 
 

Timeline/Goals
--------
12/21 - Get Droplet up, set up server (Nathaniel) (DONE)

Christmas Break - College Stuff

1/18 - Website with zoomable map, dot where user is (GMaps API) (Branch mapping)

1/18 - Display number of people and their geolocation coords (Branch multi?)

TBD - Combinding the two branches (Take array from multi branch and displaying all markers on mapping)
    - Javascript to mongo through python/flask (using ajax?)

Onwards - tbd
Instructions to Install
-----------------------
See site.

Notes
-----
* Phonegap
* phone orientation (gun?)
* Altitude (GMaps)
* look up Exo Arena (very similar)
* <a href = "https://www.lucidchart.com/invitations/accept/fcbee2ba-ad71-4424-b337-9f8603afda66">site map</a>

Game Mechanics (not set in stone)
------------------------------------
* in certain radius, press button, everyone else in it dies
* press button to get location, upload own latest
