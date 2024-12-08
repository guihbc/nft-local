from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if not w3.is_connected():
    raise Exception("Web3 not connected!")

with open("./contracts/MyNFT.abi", "r") as abi_file:
    abi = abi_file.read()

with open("./contracts/MyNFT.bin", "r") as bin_file:
    bytecode = bin_file.read()

chain_id = 1337
address = w3.eth.accounts[0] # Geth dev account
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

transaction = contract.constructor().build_transaction({
    "from": address,
    "nonce": w3.eth.get_transaction_count(address),
    "gas": 5000000,
    "gasPrice": w3.eth.gas_price,
    "chainId": chain_id
})

# signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_transaction(transaction=transaction)

receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Contract deployed at: {receipt.contractAddress}")
