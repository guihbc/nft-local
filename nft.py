from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if not w3.is_connected():
    raise Exception("Web3 not connected!")

with open("./contracts/MyNFT.abi", "r") as abi_file:
    ABI = abi_file.read()

account_address = w3.eth.accounts[0] # Geth dev account
contract_address = '0x1C2aC49C97658Cd5E970418Ca94750ab504C8654' # Deployed using ./scripts/deploy_contract.py

print(f'Using geth default account: {account_address}')
MyNFT = w3.eth.contract(address=contract_address, abi=ABI)

nft_metadata = 'http://localhost:8080/ipfs/QmPowR52BtFdReHvWfpeUqm6oHtdoVydyE14wWo9hHNDU1'
mint_tx = MyNFT.functions.mint(to=account_address, metadataURI=nft_metadata).build_transaction({
    'chainId': 1337,
    'from': account_address,
    'gas': 5000000,
    'gasPrice': w3.to_wei('20', 'gwei'),
    'nonce': w3.eth.get_transaction_count(account_address),
})

tx_hash = w3.eth.send_transaction(mint_tx)
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"transaction completed! Hash: {receipt.transactionHash.hex()}")

current_token_id = MyNFT.functions.nextTokenId().call() - 1
owner_address = MyNFT.functions.ownerOf(current_token_id).call()
print(f"The token {current_token_id} belongs to {owner_address}")

token_uri = MyNFT.functions.tokenURI(current_token_id).call()
print(f'Token URI: {token_uri}')
