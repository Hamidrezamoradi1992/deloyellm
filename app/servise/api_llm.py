import requests
import json
from config.settings import setting
class ApiLLm:
    __slots__=['massage','user',"wsclient"]
    def __init__(self,massage:str,user:str=None)->None:
        self.massage=massage
        self.user=user



    def send(self):
        url = "http://87.236.166.163:8000/ask"
        headers = {"Content-Type": "application/json"}
        datas={"question": self.massage}
        response= requests.request("POST",url=url,headers=headers,data=datas)
        del self
        return response