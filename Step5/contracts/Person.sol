// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;
import "./Car.sol";

contract Person {
    Car car;
    uint256 balance;

    constructor(address car_) {
        car = Car(car_);
        balance = 100;
    }

    function buyCar() external {
        balance -= car.price();
    }

    function viewBalance() external view returns (uint256) {
        return balance;
    }

    function get_price() external view returns (uint256) {
        return car.price();
    }
}
