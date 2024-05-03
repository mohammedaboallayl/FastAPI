import requests 

def agequery(image): 
    API_URL = "https://api-inference.huggingface.co/models/nateraw/vit-age-classifier" 

    headers = {"Authorization": "Bearer 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"} 
    try:
        response = requests.post(API_URL, headers=headers, data=image)
        return response.json()
    except Exception as e:
        return {"error",f"{e}"} 
