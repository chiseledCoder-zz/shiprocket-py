from .base import Assets

class Shipment(Assets):
	"""docstring for Shipment"""
	def __init__(self, shiprocket=None):
		super(Shipment, self).__init__(shiprocket)

	def get_shipment_details(sort=None, sort_by=None, filter=None, filter_by=None):
		return "Hello"