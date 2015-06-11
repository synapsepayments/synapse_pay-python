from ..apibits import *
from .. import Client
from . import *

class Deposit(APIResource):

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(Deposit, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "deposit")

    _api_attributes = {
        "amount" : {},
        "bank" : {},
        "date_created" : {},
        "id" : {},
        "resource_uri" : {},
        "status" : {},
        "status_url" : {},
        "user_id" : {},
    }
