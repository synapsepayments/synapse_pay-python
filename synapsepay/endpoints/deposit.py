from ..apibits import *
from ..resources import *

class DepositEndpoint(APIEndpoint):
    
    def all(self, params={}, headers={}):
        method = APIMethod("post", "/deposit/show", params, headers, self)
        json = self.client.execute(method)
        return APIList(Deposit, json['deposits'], method, self.client)
        
    def create(self, params={}, headers={}):
        method = APIMethod("post", "/deposit/add", params, headers, self)
        json = self.client.execute(method)
        return Deposit(json['deposit'], method, self.client)
        
    def micro(self, params={}, headers={}):
        method = APIMethod("post", "/deposit/micro", params, headers, self)
        json = self.client.execute(method)
        return APIList(Deposit, json['deposits'], method, self.client)
