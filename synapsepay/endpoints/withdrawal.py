from ..apibits import *
from ..resources import *

class WithdrawalEndpoint(APIEndpoint):
    
    def all(self, params={}, headers={}):
        method = APIMethod("post", "/withdraw/show", params, headers, self)
        json = self.client.execute(method)
        return APIList(Withdrawal, json['withdraws'], method, self.client)
        
    def create(self, params={}, headers={}):
        method = APIMethod("post", "/withdraw/add", params, headers, self)
        json = self.client.execute(method)
        return Withdrawal(json['withdrawal'], method, self.client)
