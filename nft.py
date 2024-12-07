from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if not w3.is_connected():
    raise Exception("Web3 not connected!")

# For tests only
account = w3.eth.account.create()
address = account.address
private_key = account.key.hex()

print(f'account: {address}\nkey: {private_key}')
contract_address = "<CONTRACT_ADDRESS>"
