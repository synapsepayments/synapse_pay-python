from ..apibits import *
from .. import Client
from . import *

class Order(APIResource):

    def update(self, params={}, headers={}):
        params = ParamsBuilder.merge({
            "order_id" : self.id,
        }, params)
        method = APIMethod("post", "/order/update", params, headers, self)
        json = self.client.execute(method)
        return self.refresh_from(json['order'], method)

    def void(self, params={}, headers={}):
        params = ParamsBuilder.merge({
            "order_id" : self.id,
        }, params)
        method = APIMethod("post", "/order/void", params, headers, self)
        json = self.client.execute(method)
        return self.refresh_from(json['order'], method)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(Order, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "order")

    _api_attributes = {
        "facilitator_fee" : {},
        "id" : {},
        "resource_uri" : {},
        "tip" : {},
        "date_settled" : {},
        "status" : {},
        "total" : {},
        "discount" : {},
        "seller" : {},
        "supp_id" : {},
        "is_buyer" : {},
        "note" : {},
        "status_url" : {},
        "account_type" : {},
        "amount" : {},
        "date" : {},
        "fee" : {},
        "ticket_number" : {},
    }
