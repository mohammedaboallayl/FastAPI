from fastapi import FastAPI,UploadFile
from PIL import Image
import numpy as np
from io import BytesIO
from Logs.detectage import agequery
from Logs.detectgander import ganderquery
from Logs.detectnameanddistance import render
app=FastAPI()

@app.post("/")
async def detect(img:UploadFile):
    lodedimg=Image.open(BytesIO(img.file.read()))
    rawbytes=BytesIO()
    lodedimg.save(rawbytes,"PNG")
    rawbytes.seek(0)
    responce=render(rawbytes.read())
    print(responce)
    if responce["state"]:
        image=np.array(lodedimg)
        faceimage=np.array(image[np.abs(responce["y2"]):np.abs(responce["y1"]),np.abs(responce["x1"]):np.abs(responce["x2"])])
        rawbytes.seek(0)
        ganders=ganderquery(rawbytes.read())
        
        im=Image.fromarray(faceimage.astype("uint8"),)
        rawbyte=BytesIO()
        im.save(rawbyte,"PNG")
        rawbyte.seek(0)
        age=agequery(rawbyte.read())
        
        gander=getHighScore(ganders)
        myage=getHighScore(age)
        
        if gander==False or myage==False:
            return {"state":False,"message":"Model Is Loading On hugging Face ","distance":0,"name":"name","age":"0","gander":"null"}
        return {"state":True,"message":"null","distance":responce["distance"],"name":responce["name"],"age":myage,"gander":gander}
    else:
        return {"state":False,"message":responce["message"],"distance":responce["distance"],"name":responce["name"],"age":"null","gander":"null"}


def getHighScore(Scores):
    
    if type(Scores)==dict:
        return False
    scorep=0.00
    label="0-10"
    for Score_ in Scores:
        if Score_["score"] > scorep:
            scorep=float(Score_["score"])
            label=Score_["label"]
    return label
    

