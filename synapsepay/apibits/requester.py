from .errors import ConnectionError

try:
    from urlparse import urlparse 
except ImportError:
    from urllib.parse import urlparse 

try:
    from urllib import quote 
except ImportError:
    from urllib.parse import quote 

import json
import requests 
requests.packages.urllib3.disable_warnings()

class Requester(object):

    @classmethod 
    def request(cls, method, url, headers, params):
        url, params = cls.prepare_params(url, headers, params, method)
        options = {
            'headers': headers, 
            'data': params, 
            'verify': False,
            'timeout': (30, 60) 
        }
        return requests.request(method, url, **options)

    @classmethod 
    def get(cls, url, params, headers):
        return cls.request('get', url, params, headers)

    @classmethod 
    def post(cls, url, params, headers):
        return cls.request('post', url, params, headers)

    @classmethod 
    def put(cls, url, params, headers):
        return cls.request('put', url, params, headers)

    @classmethod 
    def delete(cls, url, params, headers):
        return cls.request('delete', url, params, headers)

    @classmethod
    def prepare_params(cls, url, headers, params, method):
        if method in ['get', 'head', 'delete']:
            if len(params):
                url += '&' if urlparse(url).query else '?' + cls.query_string(params)
            params = None 
        elif 'Content-Type' in headers and headers['Content-Type'] == 'application/json':
            params = json.dumps(params)
        else:
            params = cls.query_string(params)
        return url, params

    @classmethod 
    def query_string(cls, params={}):
        if len(params.keys()):
            return '&'.join(cls.query_array(params))
        return ""

    @classmethod 
    def query_array(cls, params, key_prefix=None):
        ret = []
        for key in params:
            value = params[key] if isinstance(params, dict) else key
            key_suffix = cls.escape(key)

            if key_prefix:
                full_key = '%s[%s]' % (key_prefix, key_suffix) if isinstance(params, dict) else '%s[]' % (key_prefix)
            else:
                full_key = key_suffix

            if isinstance(value, list) or isinstance(value, dict):
                ret += cls.query_array(value, full_key)
            else:
                ret.append("%s=%s" % (full_key, cls.escape(value))) 
        return ret

    @classmethod 
    def escape(cls, value=''):
        return quote(str(value))



