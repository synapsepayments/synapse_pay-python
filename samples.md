# User

## Create a user

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"

# This creates an oauth client for the newly created user.
client = synapsepay.User.create({
    "email" : "localtest@crowdmade.com",
    "fullname" : "Test Account",
    "ip_address" : "11.111.11.11",
    "phonenumber" : "123456789",
    "password": "TestTest123$"
})
```


## Login as a user

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"

# Returns an oauth client for this user
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")
```


## Refresh access

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"

client = synapsepay.Client().refresh_access("d022a1855499e36b262a2c14b05656be8afd7ff1")

# Alternatively, if you already have a client"
client.refresh_access()
```


## Update a user

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

user = client.user.update({
    "fullname" : "new fullname",
    # "new_password" : "new-secret-password",
    "secret_note" : "some secret note"
})

# If you already have a user object"
user.update({
    "fullname" : "John Smith"
})
```


## Refresh a user

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

user = client.user.retrieve()

# If you already have a user object, you can refresh"
user.refresh()
```


## Search users

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

users = client.user.search("test")
```


# Bank Account

## Link a bank account

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

# Without an MFA
banks = client.banks.link({
    "username" : "synapse_nomfa",
    "password" : "test1234",
    "bank" : "Bank of America"
})
banks # this will be a list of bank accounts

# With a device based MFA
mfa = client.banks.link({
    "username" : "synapse_code",
    "password" : "test1234",
    "bank" : "Bank of America"
})
mfa # this will be a SynapsePay"BankMfaDevice instance
banks = mfa.answer("Bank of America", "test_answer") # this will be a list of bank accounts

# With a question based MFA
mfa = client.banks.link({
    "username" : "synapse_good",
    "password" : "test1234",
    "bank" : "Bank of America"
})
mfa # this will be a SynapsePay"BankMfaQuestions instance
banks = mfa.answer("Bank of America", "test_answer") # this will be a list of bank accounts
```


## Refresh a bank account

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

banks = client.banks.refresh("2174")
```

## Add a bank account

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

bank = client.banks.add({
    "fullname" : "Test Account",
    "account_num" : "1111111111",
    "routing_num" : "121000358",
    "nickname" : "Example bank account",
    "account_type" : "1",
    "account_class" : "1"
})
```


## Remove a bank account

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

bank = client.banks.remove("2175")

# Or if you have a bank object
bank.remove()
```


## List all bank accounts

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

banks = client.banks.all()
```


# Orders

## Create an order

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

order = client.orders.create({
  "amount" : "100",
  "facilitator_fee" : "1",
  "seller_id" : "3425",
  "bank_id" : "6730"
})
```

## Poll an order

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

order = client.orders.poll("903")
# only the status is set in this order, so access it via order.status
order.status
```


## Update an order

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

order = client.orders.update("903", { "status" : 0 })
# or if you have an order object
order.update({ "status" : 0 })
```


## Void an order

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

order = client.orders.void("903")
# or if you have an order object
order.void()
```


## View recent orders

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

orders = client.orders.recent()
```


# Deposits

## Create a deposit

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

deposit = client.deposits.create({
    "bank_id" : "2174",
    "amount" : "10"
})
```

## Create micro deposits

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

deposits = client.deposits.micro({
    "bank_id" : "2174",
    "amount1" : "0.07",
    "amount2" : "0.25"
})
```

## List all deposits

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

deposits = client.deposits.all()
```


# Wires

## Create an outgoing wire

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

wire = client.wires.create_outgoing({
    "account_number" : "123456790",
    "routing_number" : "064000020",
    "amount" : "1000"
})
```


## List all outgoing wires

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

wires = client.wires.all_outgoing()
```


## Create an incoming wire

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

wire = client.wires.create_incoming({
    "amount"" "10000"
})
```


## List all incoming wires

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

wires = client.wires.all_incoming()
```


# Withdrawals

## Create a withdrawal

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

withdrawal = client.withdrawals.create({
    "bank_id" : "2174",
    "amount" : "15"
})
```


## List all withdrawals

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

withdrawals = client.withdrawals.all()
```


# Cards

## Create a card

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

card = client.cards.create({
    "legal_name" : "Some Person",
    "account_number" : "123456789",
    "routing_number" : "123456789",
    "account_class" : "1",
    "account_type" : "2"
})
```

## Update a card

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

card = client.cards.update("76", {
    "legal_name" : "John Smith"
})
# Or if you have the card already
card.update({
    "legal_name" : "Jim Halpert"
})
```

## List all cards

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

cards = client.cards.all()
```


# Mass Pays

## Create a mass pay

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

# Create a mass pay with bank info
mass_pays = client.mass_pays.create({
    "mass_pays" : [
    {
        "legal_name" : "Some Person 1",
        "account_number" : "888888888",
        "routing_number" : "222222222",
        "amount" : "10.33",
        "trans_type" : "0",
        "account_class" : "1",
        "account_type" : "2",
        "user_info" : {
            "email" : "some@email.com",
            "phone_number" : "9011234567",
            "ip_address" : "some.ip.address",
            "dob" : "18/11/1989",
            "risk_score" : 10
        }
    },
    {
        "legal_name" : "Some Person 2",
        "account_number" : "888888888",
        "routing_number" : "222222222",
        "amount" : "10.33",
        "trans_type" : "0",
        "account_class" : "1",
        "account_type" : "1"
    }
    ]
})


# Create a mass pay with cards
mass_pays = client.mass_pays.create({
    "mass_pays" : [
    {
        "amount" : "20",
        "trans_type" : "0",
        "card_id" : "77"
    },
    {
        "amount" : "20",
        "trans_type" : "0",
        "card_id" : "76"
    }
    ]
})
```


## Cancel a mass pay

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

# mass_pays will be a list of mass pays, even though only one was cancelled.
mass_pays = client.mass_pays.cancel("323")

# Or if you already have a mass pay"
mass_pay.cancel()
```

## List all mass pays

```python
synapsepay.CLIENT_ID = "4528d2e0a2988064d8ac"
synapsepay.CLIENT_SECRET = "dcbf52b16040c94a35f345b7e2c285f936d673c9"
client = synapsepay.User.login("3ac38d63db58466982fe6f871c48f1", "TestTest123$")

mass_pays = client.mass_pays.all()
```
