
API_SANDBOX = "https://sandbox.synapsepay.com/api/v2"
CLIENT_ID = None
CLIENT_SECRET = None

API_BASE = "https://synapsepay.com/api/v2"

from .client import Client
from .resources import (Bank, BankMfaDevice, BankMfaQuestions, BankStatus, Card, Deposit, MassPay, Order, User, Wire, Withdrawal, )
from .endpoints import (BankEndpoint, BankMfaDeviceEndpoint, BankMfaQuestionsEndpoint, BankStatusEndpoint, CardEndpoint, DepositEndpoint, MassPayEndpoint, OrderEndpoint, UserEndpoint, WireEndpoint, WithdrawalEndpoint, )
