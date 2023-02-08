// since we need to call the function "price()" from inside 
// Car.sol, we will be referencing it via the "using" keyword.
// NOTE that this could have been avoided, if Personl.sol had inherited Car.sol
using Car as vehicle

methods {
    viewBalance() returns(uint256) envfree;
    vehicle.price() returns(uint256) envfree;
}

rule balanceDecreasesOnPurchase(env e) {
    // we now require a condition to hold before the rule is checked
    require vehicle.price() == 10;

    mathint balanceBefore = viewBalance();

    buyCar(e);

    mathint balanceAfter = viewBalance();

    assert balanceAfter < balanceBefore, 
        "balance does not decrease on purchasing a car";
}
