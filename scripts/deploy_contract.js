const { Web3 } = require('web3');
const fs = require('fs');

const web3 = new Web3('http://127.0.0.1:8545');
const { eth } = web3;

const abi = JSON.parse(fs.readFileSync('./contracts/MyNFT.abi', 'utf8'));
const bytecode = fs.readFileSync('./contracts/MyNFT.bin', 'utf8');

(async () => {
    const accounts = await eth.getAccounts();
    const account = accounts[0]; // Geth dev account

    console.info('Deploying contract')
    const contract = new eth.Contract(abi);
    
    const result = await contract
        .deploy({ data: bytecode })
        .send({
            from: account,
            gas: 5000000,
            gasPrice: web3.utils.toWei('20', 'gwei'),
        });

    console.info('Contract deployed to:', result.options.address);
})()
