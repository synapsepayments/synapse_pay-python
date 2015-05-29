from ..apibits import *
from ..resources import *

class CardEndpoint(APIEndpoint):
    
    def all(self, params={}, headers={}):
        method = APIMethod("post", "/card/show", params, headers, self)
        json = self.client.execute(method)
        return APIList(Card, json['cards'], method, self.client)
        
    def create(self, params={}, headers={}):
        method = APIMethod("post", "/card/add", params, headers, self)
        json = self.client.execute(method)
        return Card(json['card'], method, self.client)
        
    def update(self, id, params={}, headers={}):
        params = ParamsBuilder.merge({
            "id" : id,
        }, params)
        method = APIMethod("post", "/card/edit", params, headers, self)
        json = self.client.execute(method)
        return Card(json['card'], method, self.client)
