# SPOT-uploading
This repo contains files for connecting to the database and object cloud storage.

## Mongo database: ##
* Hosted on mongo atlas cloud
  * aws servers
* Connect using mongo.py, which contains methods for CRUD ops
* Frontend doesn't need the file, connects directly
* Current problems: none

## Object storage: ##
* Currently using google drive but it sucks
* Connect using driveAPITest.py
  * makes connection, but requires set address
* Frontend needs this to load images and videos
* Current problems: since address keeps jumping, we can't verify the uri

## Server: ##
Files in /web/bin
Must be authed to access

## TODO ##
Fix drive connections so files can be transferred
Build workflow for running these files from computer connected to Spot
