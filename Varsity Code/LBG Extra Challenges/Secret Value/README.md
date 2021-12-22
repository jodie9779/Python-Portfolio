## Brief Description
This was the second challenge in the challenges set by Lloyds Banking Group, and was rated as medium difficulty. It took me half an hour to complete this challenge, and I got a score of 100%. I was happy to see that I had considered all edge cases on this challenge, and had also learnt about binary search which I will definitely take forward!

## Challenge Description
Louisa has forgotten her banking app passcode. Without it, she won’t be able to transfer her friend the money they need for her ticket to the show tonight. In case Louisa forgot her passcode, she hid each digit in a separate array of numbers so that she could recover the passcode later. However, she doesn’t know which digit in each array is in her passcode. Luckily, Louisa also stored the digits as secret values on her computer. These secret values can’t be read directly to keep them secure, but if she writes a function, her computer can pass the secret values in and retrieve her passcode digits from the arrays.

When Louisa first stored her secret values, she wrote down these retrieval instructions:
* The method will accept an array of sorted integers and a secret value M
* The method will return an integer which gives the location of the secret value in the array
* For extra security, some of the secret values are fake. If the secret value is not in the array, it isn’t part of the passcode, and the method should return -1
* The secret value will lie in the range 1 <= M <= 10**5

Louisa also wrote these examples:
* If the inputs are 1,2,5,8,11,12 and M=5, the output will be 2.
* If the inputs are 2,7,9,13,18,22,31 and M=14, the output will be -1.

Combining all of the digits will give Louisa the passcode she needs. She only has a few days before her friend gives her ticket to somebody else, so she needs to make sure the code runs efficiently (hint: use binary search). She doesn’t want to miss the show!
