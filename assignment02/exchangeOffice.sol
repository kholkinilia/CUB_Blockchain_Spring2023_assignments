// SPDX-License-Identifier: MIT

pragma solidity >= 0.8.18;

// Exchange ETH to RUB and pay a fee for it!
contract exchangeRUB {

    // Declare state variables of the contract
    address public zentrobank;
    mapping (address => uint) public balanceRUB;

    // When 'ExchangeOfficee' contract is deployed:
    // 1. set the deploying address as the zentrobank
    // 2. set the deployed smart contract's RUB balance to 1000
    constructor() {
        zentrobank = msg.sender;
        balanceRUB[address(this)] = 1000;
    }

    // Allow the owner to increase the smart contract's cupcake balance
    function issue(uint amount) public {
        require(msg.sender == zentrobank, "Only the zentrobank can issue RUB.");
        balanceRUB[address(this)] += amount;
    }

    // Allow anyone to purchase cupcakes
    function buyRUB(uint amount) public payable {
        require(msg.value >= amount * 1 wei, "You must pay at least 1 Wei per RUB");
        require(balanceRUB[address(this)] >= amount, "Not enough RUB in stock to complete this purchase :(");
        balanceRUB[address(this)] -= amount;
        balanceRUB[msg.sender] += amount;
    }

    function sellRUB(uint amount) public {
        require(address(this).balance >= amount * 1 wei, "There is not enough wei on contract balance.");
        require(balanceRUB[msg.sender] >= amount, "You should have enough RUB on your account.");
        balanceRUB[msg.sender] -= amount;
        payable(msg.sender).transfer(amount * 1 wei);
    }
}
