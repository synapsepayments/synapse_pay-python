class ApibitsError(Exception):
	def __init__(self, message=None):
		self.message = message

	def __str__(self):
		return self.message


class APIError(ApibitsError):
    def __init__(self, message=None, api_method=None):
    	self.message = message 
    	self.api_method = api_method

    def code(self):
    	return self.api_method.status_code if self.api_method else None

    def body(self):
    	return self.api_method.text if self.api_method else None 

class AuthenticationError(ApibitsError):
    pass 

class ConnectionError(APIError):
    pass

