// we won't refer to 'Car.sol' here (via the 'using' keyword) and 
// let the DISPATCHER figure it out

methods {
    viewBalance() returns(uint256) envfree;
    price() returns(uint256) envfree => DISPATCHER(true);
    get_price() returns(uint256) envfree;
}

// will fail, but call to price() from inside buyCar(e) will
// succeed. The Prover will HAVOC the value to 0.
rule balanceDecreasesOnPurchase_01(env e) {
    // require price() == 10;

    mathint balanceBefore = viewBalance();

    buyCar(e);

    mathint balanceAfter = viewBalance();

    assert balanceAfter < balanceBefore, 
        "balance does not decrease on purchasing a car";
}

// will be skipped, but clicking on the skipped rule in the 
// verification report will show a problem that price() was not
// recognized as it does not exist in Person.sol contract.
// Effectively, direct calls to 'DISPATCHED' non-currentContract functions
// cannot be made.
rule balanceDecreasesOnPurchase_02(env e) {
    require price() == 10;

    mathint balanceBefore = viewBalance();

    buyCar(e);

    mathint balanceAfter = viewBalance();

    assert balanceAfter < balanceBefore, 
        "balance does not decrease on purchasing a car";
}

// will pass, since we have now wrapped the price() function inside 
// get_price() which is present in the currentContract i.e. Person.sol
rule balanceDecreasesOnPurchase_03(env e) {
    require get_price() == 10;

    mathint balanceBefore = viewBalance();

    buyCar(e);

    mathint balanceAfter = viewBalance();

    assert balanceAfter < balanceBefore, 
        "balance does not decrease on purchasing a car";
}

// NOTE:
// `DISPATCHER(true)` is able to figure out the correct contract from the scene only if the call
// to the function is NOT made directly from the spec file. It has to be from within a function of 
// the currentContract, or a contract inherited by currentContract.
