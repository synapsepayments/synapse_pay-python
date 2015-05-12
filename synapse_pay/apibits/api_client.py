from .params_builder import ParamsBuilder

class APIClient(object):
	headers = {}
	params = {}

	def execute(self, api_method):
		api_method.headers = ParamsBuilder.merge(api_method.headers, self.headers)
		api_method.params = ParamsBuilder.merge(api_method.params, self.params)
		return api_method.execute()

	def refresh_from(self, headers, params):
		self.headers = headers 
		self.params = params 
		return self 

	def __init__(self, headers, params):
		self.refresh_from(headers, params)

	# TODO: def __repl__