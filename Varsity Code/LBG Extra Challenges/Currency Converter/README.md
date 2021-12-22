## Brief Description
This was the fourth challenge in the challenges set by Lloyds Banking Group, and was rated as hard difficulty. It took me just over one hour to complete this challenge, and I got a score of 100%. I had a few troubles with this challenge, due to its complex nature. I did also spot a few bugs within this challenge, which I raised within the team. Overall I was really happy with my solution for this challenge. 

## Challenge Description
Forex trading, or FX trading, is the conversion of one currency into another. FX is one of the most actively traded markets in the world, with individuals, companies and banks carrying out around $6.6 trillion worth of forex transactions every single day. A forex pair is a combination of two currencies that are traded against each other. An example is the British Pound (base currency) against the US dollar (quote currency). Represented as GBP/USD. To buy a currency pair means that you expect the price to rise, indicating that the base currency is strengthening relative to the quote currency. To sell a currency pair means you expect the price of fall, which would happen if the base currency weakened against the quote currency. To help better understand the risks in trading currency pairs, the traders at the ABC Bank would like to create a tool that could quickly perform these currency conversions (in a dynamic way) so that they can better assess any profit that could arise from a strengthening/weakening currency pair.

They have a system they use to capture these currency pair evaluations and the output from this system is in XML and looks like this:

\<Trades>

\<Trade id='1' base='GBP' amount='10000'>\<FX quote='USD' rate='1.3629' />\<FX quote='YEN' rate='154.68' />\</Trade>

\<Trade id='2' base='GBP' amount='560000'>\<FX quote='EUR' rate='1.1796' />\<FX quote='USD' rate='1.3629' />\</Trade>

\<Trade id='3' base='GBP' amount='2000000'>\<FX quote='ZAR' rate='20.24' />\<FX quote='AUD' rate='1.85' />\</Trade>

\<Trade id='4' base='GBP' amount='143800'>\<FX quote='EUR' rate='1.1796' />\<FX quote='ZAR' rate='20.24' />\</Trade>

\<Trade id='5' base='GBP' amount='67050'>\<FX quote='YEN' rate='154.68' />\<FX quote='ZAR' rate='20.24' />\</Trade>

\<Trade id='6' base='GBP' amount='999999.98'>\<FX quote='EUR' rate='1.1796' />\<FX quote='YEN' rate='154.68' />\</Trade>

\<Trade id='7' base='GBP' amount='500.63'>\<FX quote='AUD' rate='1.85' />\<FX quote='ZAR' rate='20.24' />\</Trade>

\<Trade id='8' base='GBP' amount='1800230'>\<FX quote='AUD' rate='1.85' />\<FX quote='YEN' rate='154.68' />\</Trade>

\<Trades>

Some coding guidelines:
* Create a parent (main) function that accepts a XML string (for a single trade) containing currency pair information and return a output showing the currency conversions applied.
* Create single, re-usable helper functions - one per currency pair - that accepts a base amount and rate. Apply this function as required to perform the currency conversions.
* Use an XML parser that you feel most comfortable with, there are no restrictions here.
* There is a requirement to display the currency symbols and this should be included in the specific currency helper function.
* All currency outputs must be formatted to 2 decimal places.

Example of currency pair conversions:

INPUT: \<Trade id='1' base='GBP' amount='10000'>\<FX quote='USD' rate='1.3629' />\<FX quote='YEN' rate='154.68' />\</Trade>    
  
OUTPUT: Trade 1: GBP/USD = US$13,629.00; GBP/YEN = ¥1,546,800.00
  
INPUT: \<Trade id='2' base='GBP' amount='560000'>\<FX quote='EUR' rate='1.1796' />\<FX quote='USD' rate='1.3629' />\</Trade>  
  
OUTPUT: Trade 2: GBP/EUR = €660,576.00; GBP/USD = US$763,224.00
