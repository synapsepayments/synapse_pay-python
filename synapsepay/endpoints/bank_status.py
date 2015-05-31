from ..apibits import *
from ..resources import *

class BankStatusEndpoint(APIEndpoint):
    
    def all(self, params={}, headers={}):
        method = APIMethod("post", "/bankstatus/show", params, headers, self)
        json = self.client.execute(method)
        return APIList(BankStatus, json['banks'], method, self.client)
