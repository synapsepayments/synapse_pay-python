from .errors import AuthenticationError

import base64
import json
import platform

class HeadersBuilder(object):
    @classmethod 
    def default_headers(cls):
        user_agent = {
            'bindings_version': '0.0.2',
            'lang': 'python',
            'publisher': 'paid',
            'httplib': 'requests',
        }

        for attr, func in [['lang_version', platform.python_version],
                       ['platform', platform.platform],
                       ['uname', lambda: ' '.join(platform.uname())]]:
            try:
                val = func()
            except Exception as e:
                val = "!! %s" % (e,)
            user_agent[attr] = val

        headers = {
            'X-Paid-Client-User-Agent': json.dumps(user_agent),
            'User-Agent': 'SynapsePay/v1 PythonBindings/%s' % ('0.0.2',),
            'SynapsePay-Version': 'v2',
            "Content-Type" : "application/json",
        }

        return headers 



    @classmethod
    def build(cls, dev_headers):
        headers = cls.default_headers()
        headers.update(dev_headers)
        return headers
