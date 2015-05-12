class APIEndpoint(object):
	client = None 

	def __init__(self, client):
		self.client = client 