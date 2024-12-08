# NFT Local

### Compile the contract

```shell
./scripts/build-contract.sh
```

### Deploy the contract

```shell
source venv/bin/activate
pip install -r requirements.txt
python ./scripts/deploy_contract.py
```

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
