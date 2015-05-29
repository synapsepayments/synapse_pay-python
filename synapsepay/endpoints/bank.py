from ..apibits import *
from ..resources import *

class BankEndpoint(APIEndpoint):
    
    def add(self, params={}, headers={}):
        method = APIMethod("post", "/bank/add", params, headers, self)
        json = self.client.execute(method)
        return Bank(json['bank'], method, self.client)
        
    def all(self, params={}, headers={}):
        method = APIMethod("post", "/bank/show", params, headers, self)
        json = self.client.execute(method)
        return APIList(Bank, json['banks'], method, self.client)
        
    def link(self, params={}, headers={}):
        method = APIMethod("post", "/bank/login", params, headers, self)
        json = self.client.execute(method)
        if (json['is_mfa'] and json['response']['type'] == "questions"):
            return BankMfaQuestions(json['response'], method, self.client)
        elif (json['is_mfa'] and json['response']['type'] == "device"):
            return BankMfaDevice(json['response'], method, self.client)
        else:
            return APIList(Bank, json['banks'], method, self.client)
        
    def refresh(self, id, params={}, headers={}):
        params = ParamsBuilder.merge({
            "id" : id,
        }, params)
        method = APIMethod("post", "/bank/refresh", params, headers, self)
        json = self.client.execute(method)
        return APIList(Bank, json['banks'], method, self.client)
        
    def remove(self, bank_id, params={}, headers={}):
        params = ParamsBuilder.merge({
            "bank_id" : bank_id,
        }, params)
        method = APIMethod("post", "/bank/delete", params, headers, self)
        json = self.client.execute(method)
        return json
