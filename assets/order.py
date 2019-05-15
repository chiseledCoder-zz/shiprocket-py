import requests
import urls
from .base import Assets

class Order(Assets):
	"""docstring for Order"""
	def __init__(self, shiprocket=None):
		super(Order, self).__init__(shiprocket)

	def get_orders(self, data={}, **kwargs):
		if 'page' not in data.keys():
			raise KeyError("Page cannot be none.")
		self.url = urls.BASE_URL + urls.Order.all_orders
		return super(Order, self).get_data(self.url, data)

	def get_order(self, data={}, **kwargs):
		assert 'id' not in data.keys(), "id cannot be none."
		self.url = urls.BASE_URL + urls.Order.order_details
		return super(Order, self).get_data(self.url, data)

