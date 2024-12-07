from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if not w3.is_connected():
    raise Exception("Web3 not connected!")

# Test Account provided by ganache
address = '0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1'
private_key = '0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d'

print(f'account: {address}\nkey: {private_key}')
contract_address = "<CONTRACT_ADDRESS>"
