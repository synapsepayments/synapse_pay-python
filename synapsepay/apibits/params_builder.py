import synapsepay

class ParamsBuilder(object):
	@classmethod
	def merge(cls, *args):
		params = {}
		for other_dict in args:
			params.update(other_dict)
		return params

	@classmethod
	def default_params(cls):
		return {
            "client_id" : synapsepay.CLIENT_ID,
            "client_secret" : synapsepay.CLIENT_SECRET,
        }

	@classmethod
	def build(cls, params):
		""" Class currently does nothing, but was created to conform to spec."""
		return cls.merge(cls.default_params(), params)
