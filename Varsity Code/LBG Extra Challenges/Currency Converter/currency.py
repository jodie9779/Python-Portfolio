def solution(traderXml):
    import re
    trades = re.findall("^<Trade .*Trade>$", traderXml)
    currency_symbol = { "USD": "US$", "EUR": "€", "YEN": "¥", "ZAR": "R", "AUD": "AU$", "JPY": "¥", "GBP": "£"}
    for trade in trades:
        trade_id = re.findall("id='([0-9]+)'", trade)
        base = re.findall("base='([a-zA-Z]+)'", trade)
        base_amount = re.findall("amount='([0-9\.]+)'", trade)
        quotes = re.findall("quote='([a-zA-Z]+)'", trade)
        rates = re.findall("rate='([0-9\.]+)'", trade)
        string_output = 'Trade ' + trade_id[0] + ': '
        position = 0
        for quote in quotes:
            pair = base[0] + '/' + quote
            final_amount = float(base_amount[0]) * float(rates[position])
            finalformat = '{:,.2f}'.format(final_amount)
            symbol = currency_symbol.get(quote)
            string_output = string_output + pair + ' = ' + symbol + finalformat
            if (position+1) < len(quotes):
                string_output = string_output + '; '
            position +=1
        return string_output

