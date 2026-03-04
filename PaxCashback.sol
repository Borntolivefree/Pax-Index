// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract PaxCashback {
    address public owner;
    
    enum EthicsGrade { RED, YELLOW, GREEN }

    event CashbackDistributed(address indexed user, uint256 amount, EthicsGrade grade);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Apenas o oraculo Pax pode validar.");
        _;
    }

    /**
     * @dev Distribui o cashback com base na classificacao do Engine.py
     * @param _user Endereco do utilizador
     * @param _grade O veredicto etico (0, 1 ou 2)
     */
    function distribute(address payable _user, EthicsGrade _grade) public payable onlyOwner {
        uint256 amountToPay;

        if (_grade == EthicsGrade.GREEN) {
            // 80% de Cashback
            amountToPay = (msg.value * 80) / 100;
        } else if (_grade == EthicsGrade.YELLOW) {
            // 40% de Cashback (Defesa Civil/Fronteiras)
            amountToPay = (msg.value * 40) / 100;
        } else {
            // RED: 0% de Cashback (Guerra Ofensiva)
            amountToPay = 0;
        }

        if (amountToPay > 0) {
            _user.transfer(amountToPay);
        }

        emit CashbackDistributed(_user, amountToPay, _grade);
    }

    // Funcao para o contrato receber fundos do ecossistema
    receive() external payable {}
}
