from ..apibits import *
from ..resources import *

class WireEndpoint(APIEndpoint):
    
    def all_incoming(self, params={}, headers={}):
        method = APIMethod("post", "/wirein/show", params, headers, self)
        json = self.client.execute(method)
        return APIList(Wire, json['wires'], method, self.client)
        
    def all_outgoing(self, params={}, headers={}):
        method = APIMethod("post", "/wireout/show", params, headers, self)
        json = self.client.execute(method)
        return APIList(Wire, json['wires'], method, self.client)
        
    def create_incoming(self, params={}, headers={}):
        method = APIMethod("post", "/wirein/add", params, headers, self)
        json = self.client.execute(method)
        return Wire(json['wire'], method, self.client)
        
    def create_outgoing(self, params={}, headers={}):
        method = APIMethod("post", "/wireout/add", params, headers, self)
        json = self.client.execute(method)
        return Wire(json['wire'], method, self.client)
