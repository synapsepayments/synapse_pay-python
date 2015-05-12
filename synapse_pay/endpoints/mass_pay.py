from ..apibits import *
from ..resources import *

class MassPayEndpoint(APIEndpoint):
    
    def all(self, params={}, headers={}):
        method = APIMethod("post", "/masspay/show", params, headers, self)
        json = self.client.execute(method)
        return APIList(MassPay, json['mass_pays'], method, self.client)
        
    def cancel(self, id, params={}, headers={}):
        params = ParamsBuilder.merge({
            "id" : id,
        }, params)
        method = APIMethod("post", "/masspay/cancel", params, headers, self)
        json = self.client.execute(method)
        return APIList(MassPay, json['mass_pays'], method, self.client)
        
    def create(self, params={}, headers={}):
        method = APIMethod("post", "/masspay/add", params, headers, self)
        json = self.client.execute(method)
        return APIList(MassPay, json['mass_pays'], method, self.client)
