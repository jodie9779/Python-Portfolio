def redact_card_details(message):
    import re
    AMEX = re.findall('3[4, 7][0-9]{13}', message)
    MC = re.findall('5[1-5][0-9]{14}', message)
    VISA = re.findall('4[0-9]{12}', message)
    first_card = ''
    if len(AMEX) == 0 and len(MC) == 0 and len(VISA) == 0:
        return ["NONE", message]
    if len(AMEX) > 0:
        start_amex = message.find(AMEX[0])
        AMEX_message = message[:start_amex] + '***************' + message[start_amex + 15:]
        first_card = "AMEX"
    if len(MC) > 0:
        start_mc = message.find(MC[0])
        MC_message = message[:start_mc] + '****************' + message[start_mc + 16:]
        if first_card == 'AMEX':
            if start_mc < start_amex:
                first_card = "MASTERCARD"
        else:
            first_card = 'MASTERCARD'
    if len(VISA) > 0:
        start_visa = message.find(VISA[0])
        VISA_message = message[:start_visa] + '*************' + message[start_visa + 13:]
        if first_card == 'AMEX':
            if start_visa < start_amex:
                first_card = 'VISA'
        elif first_card == 'MASTERCARD':
            if start_visa < start_mc:
                first_card = 'VISA'
        else:
            first_card = 'VISA'
    if first_card == 'AMEX':
        return ['AMEX', AMEX_message]
    elif first_card == 'MASTERCARD':
        return ['MASTERCARD', MC_message]
    elif first_card == 'VISA':
        return ['VISA', VISA_message]

print(redact_card_details(" "))