solc-select use 0.8.0

certoraRun \
../contracts/Person.sol ../contracts/Car.sol \
--verify Person:../specs/person.spec \
--link Person:car=Car \
--solc solc \
--msg "step3"