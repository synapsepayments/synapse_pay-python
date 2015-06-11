from ..apibits import *
from .. import Client
from . import *

class BankMfaQuestions(APIResource):

    def answer(self, bank, mfa, params={}, headers={}):
        params = ParamsBuilder.merge({
            "bank" : bank,
            "mfa" : mfa,
        }, params)
        params = ParamsBuilder.merge({
            "access_token" : self.access_token,
        }, params)
        method = APIMethod("post", "/bank/mfa", params, headers, self)
        json = self.client.execute(method)
        if (json['is_mfa'] and json['response']['type'] == "questions"):
            return BankMfaQuestions(json['response'], method, self.client)
        elif (json['is_mfa'] and json['response']['type'] == "device"):
            return BankMfaDevice(json['response'], method, self.client)
        else:
            return APIList(Bank, json['banks'], method, self.client)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(BankMfaQuestions, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "bank_mfa_questions")

    _api_attributes = {
        "access_token" : {},
        "mfa" : {},
        "type" : {},
    }
