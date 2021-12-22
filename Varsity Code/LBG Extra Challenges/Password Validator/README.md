## Brief Description
This was the third challenge in the challenges set by Lloyds Banking Group, and was rated as medium difficulty. It took me just over two hour to complete this challenge, and I got a score of 100%. There was a few initial bugs within this challenge, which I spotted and raised to the team, however this lengthened my time slightly. I was still really happy as I still got 100% and was also able to make the challenge better for others!

## Challenge Description
Cybersecurity has been a priority for the banking industry for many years. Yet, despite investments in security controls, cyber-attacks keep coming. Around 1 in 4 organisations experience security breaches at least once a week. To help mitigate these risks, ABC Bank has decided to review its password policy to encourage users of the online platform to increase the complexity of their passwords, to better protect their assets.

You have been tasked with building a password validation tool for enforcing the following password rules:
* Passwords must be between 12 and 25 characters in length
* Passwords cannot contain the word 'password'
* Passwords must contain at least 1 number, 1 capital letter and 1 of these special characters: @, -, _, +, !, ?, %, $, #
* Passwords cannot have 2 or more numbers or special characters in a sequence
* Passwords cannot end with a number or a special character
* Passwords must have at least 1 run of 5 or more letters in a sequence unless your password is more than 20 characters long
* The same single character must not repeat/appear 4 or more times in a password

Coding guidelines:
* Create a function that accepts a single password and returns true or false, indicating whether or not the password supplied is valid (true = valid, false = invalid)
* Avoid the use of nested if/else statements for each rule

Examples of invalid passwords:
* This is my password! - Failed Rule 2 (cannot contain the word 'password') and Rule 5 (cannot end with a special character).
* newP@ssword234 - Failed Rule 4 (contains 3 numbers in a sequence which exceeds maximum of 2 numbers in a sequence). Failed Rule 5 (ends with a number).
* 1234$67890abc - Failed Rule 3 (no capital letter). Failed Rule 4 (contains 3 numbers in a sequence which exceeds maximum of 2 numbers in a sequence). Failed Rule 6 (password is less than 20 characters and only has a sequence of 3 letters, must contain 5 or more letters in a sequence).
* qUerTy$asdfg911GO - Failed Rule 4 (contains 3 numbers in a sequence which exceeds maximum of 2 numbers in a sequence).
* FKA#HbzNbmfsAYbOf1Y0k%Qbf - Failed Rule 7 (The letter 'b' appears 4 times in the password).
* 8PELdwo@$qnFaJKquW - Failed Rule 4 (contains 2 special characters in a sequence which exceeds maximum of 2).
* retr@ce-yEar-ginger - Failed Rule 3 (does not contain a number).
* avert-dut1ful-state - Failed Rule 3 (does not contain a capital letter)
* club,+paycheck,5prIsm - Failed Rule 3 (contains invalid character ','. This character is not a letter, number or valid special character).
