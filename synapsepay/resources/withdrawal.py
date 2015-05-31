from ..apibits import *
from .. import Client
from . import *

class Withdrawal(APIResource):

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(Withdrawal, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "withdrawal")

    _api_attributes = {
        "user_id" : {},
        "date_created" : {},
        "id" : {},
        "instant_credit" : {},
        "resource_uri" : {},
        "status_url" : {},
        "amount" : {},
        "bank" : {},
        "fee" : {},
        "status" : {},
    }
