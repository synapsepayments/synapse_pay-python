from ..apibits import *
from .. import Client
from . import *

class User(APIResource):

    @classmethod
    def create(cls, params={}, headers={}):
        method = APIMethod("post", "/user/create", params, headers, cls)
        json = method.execute()
        return Client().refresh_from(json)

    @classmethod
    def login(cls, username, password, params={}, headers={}):
        params = ParamsBuilder.merge({
            "username" : username,
            "password" : password,
        }, params)
        method = APIMethod("post", "/user/login", params, headers, cls)
        json = method.execute()
        return Client().refresh_from(json)

    @classmethod
    def refresh_access(cls, refresh_token, params={}, headers={}):
        params = ParamsBuilder.merge({
            "refresh_token" : refresh_token,
        }, params)
        method = APIMethod("post", "/user/refresh", params, headers, cls)
        json = method.execute()
        return Client().refresh_from(json)

    def refresh(self, params={}, headers={}):
        method = APIMethod("post", "/user/show", params, headers, self)
        json = self.client.execute(method)
        return self.refresh_from(json['user'], method)

    def update(self, params={}, headers={}):
        method = APIMethod("post", "/user/edit", params, headers, self)
        json = self.client.execute(method)
        return self.refresh_from(json['user'], method)

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(User, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "user")

    _api_attributes = {
        "visit_message" : {},
        "avatar" : {},
        "referral_code" : {},
        "resource_uri" : {},
        "visit_count" : {},
        "has_avatar" : {},
        "is_trusted" : {},
        "phone_number" : {},
        "username" : {},
        "accept_bank_payments" : {},
        "promo_text" : {},
        "user_id" : {},
        "seller_details" : {},
        "accept_gratuity" : {},
        "balance" : {},
        "email" : {},
        "fullname" : {},
    }
