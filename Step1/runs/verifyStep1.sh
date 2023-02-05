solc-select use 0.8.0

certoraRun \
../contracts/Person.sol \
--verify Person:../specs/person.spec \
--solc solc \
--msg "step1"