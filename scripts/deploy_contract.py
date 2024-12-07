# Did not work
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if not w3.is_connected():
    raise Exception("Web3 not connected!")

# Read your contract's ABI and bytecode
with open("./contracts/MyNFT.abi", "r") as abi_file:
    abi = abi_file.read()

with open("./contracts/MyNFT.bin", "r") as bin_file:
    bytecode = bin_file.read()

# Test Account provided by ganache
address = '0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1'
private_key = '0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d'
chain_id = 1337

contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Build and sign transaction
transaction = contract.constructor().build_transaction({
    "from": address,
    "nonce": w3.eth.get_transaction_count(address),
    "gas": 8000000,
    "gasPrice": w3.eth.gas_price,
    "chainId": chain_id
})

signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

# Wait for deployment to complete
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Contract deployed at: {receipt.contractAddress}")
