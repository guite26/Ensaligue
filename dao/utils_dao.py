from typing import Dict
def updateobj(obj, data:Dict):
    for key, value in data.items():
        setattr(obj, key, value) 