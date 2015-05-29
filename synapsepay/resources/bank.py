from ..apibits import *
from .. import Client
from . import *

class Bank(APIResource):

    def remove(self, params={}, headers={}):
        params = ParamsBuilder.merge({
            "bank_id" : self.id,
        }, params)
        method = APIMethod("post", "/bank/delete", params, headers, self)
        json = self.client.execute(method)
        return json

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(Bank, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "bank")

    _api_attributes = {
        "bank_name" : {},
        "email" : {},
        "is_buyer_default" : {},
        "is_seller_default" : {},
        "account_class" : {},
        "address" : {},
        "balance" : {},
        "account_number_string" : {},
        "id" : {},
        "resource_uri" : {},
        "nickname" : {},
        "phone_number" : {},
        "routing_number_string" : {},
        "account_type" : {},
        "date" : {},
        "mfa_verifed" : {},
        "name_on_account" : {},
    }
