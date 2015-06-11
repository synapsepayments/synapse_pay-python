from .apibits import APIClient, APIMethod

class Client(APIClient):
	_user = None
	_banks = None
	_bank_mfa_devices = None
	_bank_mfa_questions = None
	_bank_statuses = None
	_cards = None
	_deposits = None
	_mass_pays = None
	_orders = None
	_wires = None
	_withdrawals = None


	def __init__(self):
		pass

	def refresh_from(self, json):
		self.json = json
		self.oauth_consumer_key = self.json['oauth_consumer_key']
		self.refresh_token = self.json['refresh_token']
		self.expires_at = self.json['expires_at']
		self.expires_in = self.json['expires_in']

		super(Client, self).refresh_from({}, {'oauth_consumer_key': self.oauth_consumer_key})
		return self

	@classmethod
	def login(cls, username, password):
		params = {'username': username, 'password': password}
		method = APIMethod("post", "user/login", params, {}, cls)
		return cls().refresh_from(method.execute())

	def refresh_access(self, refresh_token=None):
		params = {'refresh_token': refresh_token or self.refresh_token}
		method = APIMethod("post", "/user/refresh", params, {}, self.__class__)

		return self.refresh_from(method.execute())


	@property
	def user(self):
		from .endpoints import UserEndpoint
		if not self._user:
			self._user = UserEndpoint(self)
		return self._user

	@property
	def banks(self):
		from .endpoints import BankEndpoint
		if not self._banks:
			self._banks = BankEndpoint(self)
		return self._banks

	@property
	def bank_mfa_devices(self):
		from .endpoints import BankMfaDeviceEndpoint
		if not self._bank_mfa_devices:
			self._bank_mfa_devices = BankMfaDeviceEndpoint(self)
		return self._bank_mfa_devices

	@property
	def bank_mfa_questions(self):
		from .endpoints import BankMfaQuestionsEndpoint
		if not self._bank_mfa_questions:
			self._bank_mfa_questions = BankMfaQuestionsEndpoint(self)
		return self._bank_mfa_questions

	@property
	def bank_statuses(self):
		from .endpoints import BankStatusEndpoint
		if not self._bank_statuses:
			self._bank_statuses = BankStatusEndpoint(self)
		return self._bank_statuses

	@property
	def cards(self):
		from .endpoints import CardEndpoint
		if not self._cards:
			self._cards = CardEndpoint(self)
		return self._cards

	@property
	def deposits(self):
		from .endpoints import DepositEndpoint
		if not self._deposits:
			self._deposits = DepositEndpoint(self)
		return self._deposits

	@property
	def mass_pays(self):
		from .endpoints import MassPayEndpoint
		if not self._mass_pays:
			self._mass_pays = MassPayEndpoint(self)
		return self._mass_pays

	@property
	def orders(self):
		from .endpoints import OrderEndpoint
		if not self._orders:
			self._orders = OrderEndpoint(self)
		return self._orders

	@property
	def wires(self):
		from .endpoints import WireEndpoint
		if not self._wires:
			self._wires = WireEndpoint(self)
		return self._wires

	@property
	def withdrawals(self):
		from .endpoints import WithdrawalEndpoint
		if not self._withdrawals:
			self._withdrawals = WithdrawalEndpoint(self)
		return self._withdrawals

