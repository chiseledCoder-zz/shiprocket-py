
class Assets(object):
	"""docstring for Assets"""
	def __init__(self, shiprocket=None):
		self.shiprocket = shiprocket

	def get_data(self, url, payload):
		return self.shiprocket.get_request(url, payload)

	def post_data(self, url, params):
		return self.shiprocket.post_request(url, payload)