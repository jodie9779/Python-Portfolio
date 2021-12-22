## Brief Description
This was the first challenge in the challenges set by Lloyds Banking Group, and was rated as hard difficulty. It took me just over an hour to complete this challenge, and I got a score of 67%. I wasn't the happiest with this score, as I thought I had covered all edge cases, but I was still happy that I had a working solution.

## Challenge Description
You’ve been assigned with assisting XYZ bank. XYZ Bank are building an application to better help the victims of fraud to understand why their accounts were targeted. The product owner for the application suggests one way of identifying why fraudulent activity has occurred is by finding the median transaction. This would be a more reliable metric than the mean transaction, which could be skewed by an unusual large transaction.

The proposed plan is as follows:
* Validate whether the two example accounts given are valid.
* Extract and format the transactions into an array of decimals.
* Find the median transaction of all valid transactions.

[Extra information]

A valid account is an array of strings that contain:
* An eight digit account number of the form: 'XXXXXXXX', where X is an integer.
* A sort code of the form: 'XX-XX-XX' or 'XXXXXX', where X is an integer.
* One or more valid transactions.
* A transaction is a string that:
  * May or may not be prefixed with a pound (£) sign.
  * Must include a decimal point.
  * Does not start with a 0, unless the value is under £1.

Some Examples:
* '£100.89' is a valid transaction.
* '0.99' is a valid transaction.
* '10.99' is a valid transaction.
* '07.11' is NOT a valid transaction.
* '£0.981' is NOT a valid transaction.

An example input of two valid accounts is below:

\['12345679', '12-34-57','1.00', '2.00', '3.00'], \['12345678', '12-34-56', '1.00','2.00','3.00']

Things to Consider:
* If an empty input is given, then return the value -1.0
* If either account is invalid, then return the value -1.0
