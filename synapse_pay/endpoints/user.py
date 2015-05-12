from ..apibits import *
from ..resources import *

class UserEndpoint(APIEndpoint):
    
    def retrieve(self, params={}, headers={}):
        method = APIMethod("post", "/user/show", params, headers, self)
        json = self.client.execute(method)
        return User(json['user'], method, self.client)
        
    def search(self, query, params={}, headers={}):
        params = ParamsBuilder.merge({
            "query" : query,
        }, params)
        method = APIMethod("post", "/user/customers", params, headers, self)
        json = self.client.execute(method)
        return APIList(User, json['customers'], method, self.client)
        
    def update(self, params={}, headers={}):
        method = APIMethod("post", "/user/edit", params, headers, self)
        json = self.client.execute(method)
        return User(json['user'], method, self.client)
