#!/bin/bash

solc --base-path . --include-path node_modules --abi --bin nft.sol -o contracts/
