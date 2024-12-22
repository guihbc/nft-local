# NFT Local

This project is compiling an Smart Contract, deploying it to the Ethereum Network (Docker container), creating an NFT Metadata and
calling the contract to mint the NFT.

### Requirements

- Docker
- Node.js
- Python
- [Solc (Solidity compiler)](https://docs.soliditylang.org/en/latest/installing-solidity.html)

### Compile the contract

```shell
npm install
```

Need to use `npm install` to get the openzeppelin contracts

```shell
./scripts/build-contract.sh
```

The `./scripts/build-contract.sh` is a shell script to compile the solidity contract and saves to the `contracts/` folder

### Containers start

```shell
docker compose up
```

Or if using docker compose V1

```shell
docker-compose up
```

### Deploy the contract

```shell
pip install -r requirements.txt
python ./scripts/deploy_contract.py
```

The `./scripts/deploy_contract.py` is a Python Script to deploy the contract to the blockchain

### Send image to ipfs

```shell
curl -X POST -F file=@./nft/sun.jpg "http://localhost:5001/api/v0/add"
```

Access file: http://localhost:8080/ipfs/{hash}

### Send metadata to ipfs

```shell
curl -X POST -F file=@./nft/sun_metadata.json "http://localhost:5001/api/v0/add"
```

Access file: http://localhost:8080/ipfs/{hash}

### Solidity mint function call

```shell
python nft.py
```

This file `nft.py` is where the deployed contract is called to mint the NFT
