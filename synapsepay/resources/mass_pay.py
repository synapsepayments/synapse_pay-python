from ..apibits import *
from .. import Client
from . import *

class MassPay(APIResource):

    def cancel(self, params={}, headers={}):
        params = ParamsBuilder.merge({
            "id" : self.id,
        }, params)
        method = APIMethod("post", "/masspay/cancel", params, headers, self)
        json = self.client.execute(method)
        return APIList(MassPay, json['mass_pays'], method, self.client)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(MassPay, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "mass_pay")

    _api_attributes = {
        "account_number_string" : {},
        "amount" : {},
        "date" : {},
        "fee" : {},
        "id" : {},
        "name_on_account" : {},
        "resource_uri" : {},
        "routing_number_string" : {},
        "status" : {},
        "trans_type" : {},
    }
