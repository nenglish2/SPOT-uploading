# SPOT-uploading
This repo contains files for connecting to the database and object cloud storage.
Mongo database:
* Hosted on mongo atlas cloud
  * aws servers
* Connect using mongo.py, which contains methods for CRUD ops
* Frontend doesn't need the file, connects directly

Object storage:
* Currently using google drive but it sucks
* Connect using driveAPITest.py
  * makes connection, but requires set address
* 
