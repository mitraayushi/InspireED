// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyCustomToken is ERC20, Ownable {
    constructor() ERC20("InspireEDToken", "InspED") Ownable(msg.sender) {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    function transfer(address to, uint256 amount) public override returns (bool){
        _transfer(_msgSender(), to, amount);
        return true;
    }

    function donate(address donor, address receiver, uint256 amount) public returns (bool) {
        require(donor != address(0), "Donor address cannot be zero");
        require(receiver != address(0), "Receiver address cannot be zero");
        require(balanceOf(donor) >= amount, "Donor has insufficient balance");

        _transfer(donor, receiver, amount);
        return true;
    }
}
