# £1 into account on Monday (day 1), then £1 more than day before
# On each subsequent Monday, it is £1 more than the previous Monday

def number_of_days_to_save(moneysaved):
    decimalpoints = str(moneysaved)[::-1].find('.')
    try:
        moneysaved = int(moneysaved)
    except ValueError:
        return -1
    if moneysaved < 0:
        return -1
    elif moneysaved > 74926:
        return -1
    elif decimalpoints > 2:
        return -1
    else:
        totalmoney = 0
        week = 1
        day = 0
        while totalmoney < moneysaved:
            if day % 7 == 0 and day != 0:
                week +=1
                day = 0
            totalmoney += week + day
            day += 1
        daysneeded = 7 * (week - 1) + day
        return daysneeded






print('correct answer = 4. My answer = ', number_of_days_to_save(8.630))
print('correct answer = 10. My ansewer = ', number_of_days_to_save(36))