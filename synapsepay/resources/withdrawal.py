from ..apibits import *
from .. import Client
from . import *

class Withdrawal(APIResource):

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(Withdrawal, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "withdrawal")

    _api_attributes = {
        "amount" : {},
        "bank" : {},
        "date_created" : {},
        "fee" : {},
        "id" : {},
        "instant_credit" : {},
        "resource_uri" : {},
        "status" : {},
        "status_url" : {},
        "user_id" : {},
    }
