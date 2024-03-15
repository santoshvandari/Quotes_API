from typing import Union
from fastapi import FastAPI
from allrequests import getquotes, addquotes,deletequotes,updatequotes

app = FastAPI()


@app.get("/")
def quotes():
    return getquotes()

@app.post("/add/")
async def addquote(quotes: str, author: str):
    quotes= quotes.strip()
    author= author.strip()
    if len(quotes) == 0 or len(author) == 0:
        return {"error": "Quotes and Author are required"}
    return addquotes(quotes,author)

@app.delete("/delete/")
async def deletequote(id):
    id=id.strip()
    if id is None:
        return {"error":"ID Cannot be Empty"}
    return deletequotes(id)


@app.put("/update/")
async def updatequote(id:str,quotes:str,author:str):
    id=id.strip()
    quotes= quotes.strip()
    author= author.strip()
    if len(quotes) == 0 and len(author) == 0:
        return {"error":"Quotes Or Author are required"}
    if id is None:
        return {"error":"Please Pass the ID Too"}
    if len(quotes) == 0:
        return updatequotes("None",author,id)
    elif len(author) == 0:
        return updatequotes(quotes,"None",id)
    return updatequotes(quotes,author,id)
