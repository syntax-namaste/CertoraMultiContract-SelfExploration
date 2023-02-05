methods {
    viewBalance() returns(uint256) envfree;
}

rule balanceDecreasesOnPurchase(env e) {
    mathint balanceBefore = viewBalance();

    buyCar(e);

    mathint balanceAfter = viewBalance();

    assert balanceAfter < balanceBefore, 
        "balance does not decrease on purchasing a car";
}