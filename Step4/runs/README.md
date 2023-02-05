# Run Analysis

## Reports
### verifyStep4.sh: [Verification Report](https://prover.certora.com/output/52228/40c9e4f5c6644ba18d7f5ca9aaa7ab96?anonymousKey=d756cc3443be51ce7787ecb6b35ea0b05731ca1b)<br>

## Analysis
### verifyStep4.sh: 
![verifyStep4](images/verifyStep4.png)<br><br>

Manually adding the `require` statement that the price of the car should always be 10 does the job for us. (Check updated rule `balanceDecreasesOnPurchase` in `person.spec`).<br><br>

Since the price of the car always remains 10, shoudn't we do this via `invariants`? Let us try that as our next step.
