from ..apibits import *
from ..resources import *

class BankMfaDeviceEndpoint(APIEndpoint):
    
    def answer(self, access_token, bank, mfa, params={}, headers={}):
        params = ParamsBuilder.merge({
            "access_token" : access_token,
            "bank" : bank,
            "mfa" : mfa,
        }, params)
        method = APIMethod("post", "/bank/mfa", params, headers, self)
        json = self.client.execute(method)
        return APIList(Bank, json['banks'], method, self.client)
