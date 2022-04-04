import pandas as pd
from pymongo import MongoClient
from bson.objectid import ObjectId 
import json
import certifi
ca = certifi.where()

CLIENT = ""

class mongo:
    
    def __init__(self):
        
        self.client = MongoClient(CLIENT, tlsCAFile=ca) 
        print(self.client)
        print(self.client['HOST'])
        self.db = self.client.spot
        self.coll = self.db.data
    
    
    ###################################################
    #              GENERAL TEST METHODS   
    ##################################################
    
    def findOne(self):
        found = self.coll.find_one()
        print(found)
        return found
        
    def findAll(self):   
        found = self.coll.find();
        for x in found:
            print(x)
        return found

    ###################################################
    #           USEFUL METHODS FOR SPOT UPLOADS
    ##################################################
    
    def mongoimport(self, csv_path='C:/Users/Gchar/Documents/Colby/CS/430/test.csv'):
        ''' Imports a csv file at path csv_name to a mongo collection
        returns: count of the documents in the new collection
        '''
        self.data = pd.read_csv(csv_path)
        res = self.coll.insert_one(self.data.to_dict(orient='list'))
        
        print(res.acknowledged)
        print(res.inserted_id)
        return self.coll.count_documents({})
        

    ###################################################
    #           USEFUL METHODS FOR FRONTEND
    ##################################################
    
    def setCollection(coll):
        if coll == 'data':
            self.coll = self.db.data
    
    def getCollection(self):
        return self.coll
    
    def filterQuery(self, filter={"data_type":"photo"}):
        found = self.coll.find(filter)
        for x in found:
            print('here')
            print(x)
        return found
    
    def update(self, filter={"data_type": "photo"}, newVals={"$set":{"time":"15:30:05"}}):
        return self.coll.update_many(filter, newVals)

    def delete(self, filter={"_id":ObjectId('622bade2eae1387848b0f530')}):
        return self.coll.delete_one(filter)   
        
        
    ###################################################
    #           ADD. POSSIBLE METHODS (TBD)
    ##################################################
    
    '''

    def mongoimport_many():
        Imports multiple csv files at path csv_name to a mongo collection
        returns: count of the documants in the new collection
        client = MongoClient(db_url, db_port)
        db = client[db_name]
        coll = db[coll_name]
        data = pd.read_csv(csv_path)
        payload = json.loads(data.to_json(orient='records'))
        coll.remove()
        inserted = coll.insert_many(payload)
        return coll.count()
        #mod above

    

    def mongoimport_id():
        Imports multiple csv files at path csv_name to a mongo colection
        returns: count of the documants in the new collection
    
       client = MongoClient(db_url, db_port)
        db = client[db_name]
        coll = db[coll_name]
        data = pd.read_csv(csv_path)
        payload = json.loads(data.to_json(orient='records'))
        coll.remove()
        inserted = coll.insert_many(payload)
        return coll.count()
        #set IDs
        #mod above


    
    

    def name_and_address():
        for x in coll.find({}, {"_id": 0, "name": 1, "address": 1}):
            print(x)
    

    def no_address():     
        for x in coll.find({}, {"address": 0}):
            print(x)    
    

    def sort_alphabetically(order):
        doc = coll.find().sort("name", """-1 or 1""")
        for x in doc:
                print(x) 


    def delete_many():
        query = {"address": {"$regex":""}}
        coll.delete_many(query)


    def delete_all():
        coll.delete_many({})


    def drop_coll():
        coll.drop()


    def update_address():
        query = {"address": ""}
        new_vals = {"$set": {"address":""}}
        coll.update_one(query, new_vals)
    

    def update_many():
        query = {"address": {"$regex": ""}}
        new_vals = {"$set": {"name":""}}
        coll.update_many(query, new_vals)
    

    def limit():
        result = coll.find().limit(mod)
    '''


###################################################
#           TEST FOR RUNNING
##################################################

def main():
    inst = mongo()
    #inst.mongoimport()
    #inst.findOne()
    #inst.findAll();
    #inst.filterQuery()
    #inst.update()
    #inst.delete()
    print(inst.getCollection())

main()

