from .base import Assets
import requests
import urls

class Courier(Assets):
	"""docstring for Courier"""
	def __init__(self, shiprocket=None):
		super(Courier, self).__init__(shiprocket)

	def get_couriers(self, data={}, **kwargs):
		if 'order_id' not in data.keys():
			assert data['pickup_postcode'] is not None, 'Pickup postcode cannot be none.'
			assert data['delivery_postcode'] is not None, 'Drop postcode cannot be none.'
			assert data['cod'] is not None, 'If cod then enter 1 else enter 0 for prepaid order.'
			assert data['weight'] is not None, 'Mention package weight in kgs.'
		self.url = urls.BASE_URL + urls.Courier.check_serviceability
		return super(Courier, self).get_data(self.url, data)

	def get_international_couriers(self, data={}, **kwargs):
		if 'order_id' not in data.keys():
			assert data['cod'] is not None, 'If cod then enter 1 else enter 0 for prepaid order.'
			assert data['weight'] is not None, 'Mention package weight in kgs.'
			assert data['delivery_country'] is not None, 'Delivery country alpha-2 code required.'
		self.url = urls.BASE_URL + urls.Courier.check_international_serviceability
		return super(Courier, self).get_data(self.url, data)

