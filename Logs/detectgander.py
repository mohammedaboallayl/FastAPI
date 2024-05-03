import requests 

def ganderquery(img):  
    API_URL = "https://api-inference.huggingface.co/models/rizvandwiki/gender-classification" 
    headers = {"Authorization": "Bearer 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"} 
    try:
        response = requests.post(API_URL, headers=headers, data=img) 
        return  response.json() 
    except Exception as e:
        return {"error",f"{e}"}