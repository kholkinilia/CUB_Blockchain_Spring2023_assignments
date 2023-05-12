// interact.js

const API_KEY = process.env.API_KEY;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS;

const { ethers } = require("hardhat");
const contract = require("../artifacts/contracts/HelloWorld.sol/HelloWorld.json");

// provider - Etherscan
const provider = new ethers.providers.EtherscanProvider(network="sepolia", API_KEY);

// signer - you
const signer = new ethers.Wallet(PRIVATE_KEY, provider);

// contract instance
const helloWorldContract = new ethers.Contract(CONTRACT_ADDRESS, contract.abi, signer);

async function main() {
    const message = await helloWorldContract.message();
    console.log(`The message: ${message}`);
    console.log('Updating the message...');

    const tx = await helloWorldContract.update("New message");
    await tx.wait();

    const newMessage = await helloWorldContract.message();
    console.log(`New message: ${newMessage}`);
}

main()
    .then(() => process.exit(0))
    .catch(error => {
        console.error(error);
        process.exit(1);
    });
