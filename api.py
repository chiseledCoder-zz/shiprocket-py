import requests
import urls
import json
from config import ConfigToken, ConfigHeader
from requests.auth import AuthBase
import assets
from types import ModuleType

ASSETS = {}

for name, module in assets.__dict__.items():
	if isinstance(module, ModuleType) and name.capitalize() in module.__dict__:
		ASSETS[name] = module.__dict__[name.capitalize()]

class TokenAuth(AuthBase):
	def __init__(self, token):
		self.token = token


	def __call__(self, r):
		print(self.token)
		r.headers['Authorization'] = "Bearer " + f'{self.token}'
		return r


class Shiprocket(object):

	def __init__(self):
		self.email = None
		self.password = None
		self.token = None
		self.session = requests.Session()
		for name, Klass in ASSETS.items():
			setattr(self, name, Klass(self))

	# def build_headers(self):
	# 	if token is None:

	def authenticate(self, email, password):
		self.email = email
		self.password = password
		self.payload = {
			"email": self.email,
			"password": self.password
		}
		self.url = urls.BASE_URL + urls.Authentication.access_token
		req = requests.post(self.url, data=self.payload)
		if req.status_code == 200:
			resp = json.loads(req.text)
			self.token = str(resp['token'])
			return json.dumps({"message": "User authenticate", "status": 1})

	def get_request(self, url, data, auth=None):
		self.url = url
		self.data = data
		req = self.session.get(self.url, json=self.data, auth=TokenAuth(self.token))
		print(req.json())
		return req.json()

	def post_request(self, url, data, auth=None):
		self.url = url
		self.data = data
		req = self.session.get(self.url, data=self.data, auth=TokenAuth(self.token))
		print(req.json())
		return req.json()


rocket = Shiprocket()
rocket.authenticate(email="niks_kool007@yahoo.com", password="ashcube@123")


