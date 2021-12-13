## Brief Description
This was the fifth challenge in Varsity Code 2021, which was set by Nationwide. It took me just over 30 minutes to complete this challenge, and I got a score of 64%. The moment I seen my score, I realised my mistake. I failed to consider edge cases where there is multiple cards within the text that need starred out, and instead only starred out the first card my code found. I had thought of this when I first read the challenge, however forgot to implement it. To better improve myself for future challenges, I will try writing down all considerations I need to think about before writing my code, then check my code for these once I have written it.

## Challenge Description
Sometimes when members use our online services they may accidentally disclose private information with Arti, our online chatbot. It is important that when this happens the data is redacted so the information is not stored. Write a method to redact data shared in this way with Arti. Your solution should identify if the string contains a card number and return an array of strings. The array should contain a string for each card number indicating the card distributor (displayed in the order they are identified in the message) and another string containing the original message with any necessary redactions.

Things to consider:
* The card distributors that may be returned as a string in the array are "AMEX", "MASTERCARD" and "VISA".
* If no card number is present in the message string, the returned card distributor should be a single string within the array: "NONE".
* If data needs to be redacted, it should be replaced with asterix's indicating the length of the redacted data.

Card distributors are identified by the following method:
* AMEX: length: 15 digits, prefixes: '34', '37',
* MASTERCARD: length: 16 digits, prefixes: '51', '52', '53', '54', '55',
* VISA: length: 13 digits, prefixes: '4',

So, for example, if the input for your method is "This is a secret but my card number is 4000000000000! Shhhh! Don't tell anyone!", your method is expected to return: "VISA", "This is a secret but my card number is ************* ! Shhh! Don't tell anyone!"

Your solution should be able to handle empty string inputs and whitespace. It should also only obfuscate data which is specifically a card number. Finally, remember that the solution should return the first card identified, and should not pick up cards contained 'within' another card number.

For example: "54114111111111111" should return a "MASTERCARD" value, not a "VISA" value.
