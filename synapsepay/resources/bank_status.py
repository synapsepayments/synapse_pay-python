from ..apibits import *
from .. import Client
from . import *

class BankStatus(APIResource):

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(BankStatus, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "bank_status")

    _api_attributes = {
        "bank_name" : {},
        "date" : {},
        "id" : {},
        "logo" : {},
        "resource_uri" : {},
        "status" : {},
    }
