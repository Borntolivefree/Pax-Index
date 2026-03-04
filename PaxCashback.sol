// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract PaxIndexCashback {
    address public founder;
    uint256 public constant USER_SHARE = 80; 

    constructor() {
        founder = msg.sender;
    }

    function distributeProfit(address payable _user) public payable {
        require(msg.value > 0, "Lucro invalido");
        uint256 userAmount = (msg.value * USER_SHARE) / 100;
        _user.transfer(userAmount);
    }
}
