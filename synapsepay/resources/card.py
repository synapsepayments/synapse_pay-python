from ..apibits import *
from .. import Client
from . import *

class Card(APIResource):

    def update(self, params={}, headers={}):
        params = ParamsBuilder.merge({
            "id" : self.id,
        }, params)
        method = APIMethod("post", "/card/edit", params, headers, self)
        json = self.client.execute(method)
        return self.refresh_from(json['card'], method)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(Card, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "card")

    _api_attributes = {
        "account_class" : {},
        "account_number_string" : {},
        "account_type" : {},
        "id" : {},
        "name_on_account" : {},
        "resource_uri" : {},
        "routing_number_string" : {},
    }
