from wsgiref import headers
import requests
import json
import base64

class SalesforceConfig:
    def __init__(self):
        self.params = {
            "client_id" : "3MVG9pRzvMkjMb6nkdK55eZOxDcK1_GKVaCaVE7A0unETwkZv33NeA0iCa6zRBymc.qctit5_FEQlBJXuPhHF",
            "client_secret" : "D3DA8FB2F3E9BA40B32CFFF0A63ABA4F2B1D828D63FF786A946EC0162ABF338D",
            "username" : "mehulsinh.vaghela@vedity.com",
            "password" : "Vedity@123",
            "grant_type" : "password"
        }

        self.r = requests.post("https://login.salesforce.com/services/oauth2/token",params=self.params)
        self.access_token = self.r.json().get("access_token")
        self.instance_url = self.r.json().get("instance_url")

        # print("instance_url",instance_url)
        # print("access_token",access_token)

    def sf_call(self,action,parameters={},method='get',data={}):
        headers={
            'Content_type' : 'application/json',
            'Accept_Encoding' : 'gzip',
            'Authorization' : 'Bearer '+self.access_token
        }
        
        if method=='get':
            r = requests.request(method,self.instance_url+action,headers=headers,params=parameters,timeout=30)
        elif method in['post','patch']:
            r = requests.request(method,self.instance_url+action,headers=headers,json=data,params=parameters,timeout=10)
        else:
            raise ValueError('Method be should either get or post or patch')
        
        if r.status_code<300:
            if method=='patch':
                return None
            else:
                return r.json()
        else:
            raise Exception("API error with calling URL")

