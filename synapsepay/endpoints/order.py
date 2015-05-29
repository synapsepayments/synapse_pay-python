from ..apibits import *
from ..resources import *

class OrderEndpoint(APIEndpoint):
    
    def create(self, params={}, headers={}):
        method = APIMethod("post", "/order/add", params, headers, self)
        json = self.client.execute(method)
        return Order(json['order'], method, self.client)
        
    def poll(self, order_id, params={}, headers={}):
        params = ParamsBuilder.merge({
            "order_id" : order_id,
        }, params)
        method = APIMethod("post", "/order/poll", params, headers, self)
        json = self.client.execute(method)
        return Order(json['order'], method, self.client)
        
    def recent(self, params={}, headers={}):
        method = APIMethod("post", "/order/recent", params, headers, self)
        json = self.client.execute(method)
        return APIList(Order, json['orders'], method, self.client)
        
    def update(self, order_id, params={}, headers={}):
        params = ParamsBuilder.merge({
            "order_id" : order_id,
        }, params)
        method = APIMethod("post", "/order/update", params, headers, self)
        json = self.client.execute(method)
        return Order(json['order'], method, self.client)
        
    def void(self, order_id, params={}, headers={}):
        params = ParamsBuilder.merge({
            "order_id" : order_id,
        }, params)
        method = APIMethod("post", "/order/void", params, headers, self)
        json = self.client.execute(method)
        return Order(json['order'], method, self.client)
