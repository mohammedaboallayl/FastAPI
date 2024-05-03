
import requests

# https://mohammedallyl-mc.hf.space/
def render(img):
    try:
        response = requests.post("https://mohammedallyl-mc.hf.space/upload",files={"img":img}) 
        return response.json() 
    except Exception as error:
        return {'state': False, 'message': f'{error}', 'distance': 0, 'name': 'fekry', 'x1': 0, 'x2': 0, 'y1': 0, 'y2': 0}
