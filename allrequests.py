from DB.db import db
import random
from bson import ObjectId

def getquotes():
    quotes= list(db.quotes.find())
    if len(quotes)==0:
        return {"error" : "No Quotes Found"}
    quote= quotes[random.randint(0,len(quotes)-1)]
    return {"id":str(quote["_id"]),"quotes": quote["quotes"], "author": quote["author"]}

def addquotes(quotes: str, author: str):
    try:
        db.quotes.insert_one({'quotes': quotes,'author': author})
        return {"success":"Quotes Added Successfully"}
    except Exception as e:
        return {"error": str(e)}
    
def updatequotes(quotes:str="None",author:str="None", id:any=None):
    try:
        if id is None:
            return {"error":"ID Cannot be Empty"}
        id=ObjectId(id)
        if quotes=="None":
            print("Enter into Null Quotes")
            db.quotes.update_one({'_id':id},{'$set':{'author':author}})
            return {"success":"Author Updated Successfully"}
        elif author=="None":
            print("Enter into Null author")
            db.quotes.update_one({'_id':id},{'$set':{'quotes':quotes}})
            return {"success":"Quotes Updated Successfully"}
        db.quotes.update_one({'_id':id},{'$set':{'quotes':quotes,'author':author}})
        return {"success":"Quotes Updated Successfully"}
    except Exception as ex:
        return {"error": str(ex)}

def deletequotes(id):
    try:
        quote_id=ObjectId(id)
        db.quotes.delete_one({'_id':quote_id})
        return {"success":"Quotes Deleted Successfully"}
    except Exception as e:
        return {"error": str(e)}