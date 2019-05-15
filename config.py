
class ConfigToken: 
	def __init__(self): 
		self._token = 0
	   
	# function to get value of token 
	def get_token(self):
		return self._token
	   
	# function to set value of token 
	def set_token(self, tkn):
		self._token = tkn
  
	# function to delete token attribute 
	def del_token(self): 
		del self._token
	 
	token = property(get_token, set_token, del_token)

# print(ship.token)

class ConfigHeader(object):
	def __init__(self):
		self.headers = {
			"Authorization": None,
			"Accept": "application/json",
			"Content-Type":"application/json"
		}

	def get_headers(self):
		return self.headers

	def __getitem__(self, key):
		if key not in self.headers:
			raise KeyError
		else:
			return self.headers[key]

	def __setitem__(self, key, value):
		if key not in self.headers:
			raise KeyError
		else:
			self.headers[key] = value