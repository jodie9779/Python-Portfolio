def calculate_bag_total(items, discounts):
    item_codes = dict()
    item_prices = dict()
    for item in items:
        item_codes[item[:3]] = item_codes.get(item[:3], 0) + 1
        item_prices[item[:3]] = item_prices.get(item[:3], item[3:])
    item_new_prices = item_prices.copy()
    for discount in discounts:
        discount_item_code = discount[:3]  # Gets item code
        number_matching = discount[3:4]
        discount_category = discount[4:5]
        discount_amount = discount[5:]
        if discount_item_code in item_codes:
            if int(number_matching) <= int(item_codes[discount_item_code]):
                before_price = int(item_prices[discount_item_code])
                if discount_category == 'P':
                    after_price = before_price - before_price / 100 * int(discount_amount)
                    if int(item_new_prices[discount_item_code]) > after_price > 0:
                        item_new_prices[discount_item_code] = after_price
                elif discount_category == 'C':
                    after_price = before_price - int(discount_amount)
                    if int(item_new_prices[discount_item_code]) > after_price > 0:
                        item_new_prices[discount_item_code] = after_price
    total_price = 0
    for key in item_prices:
        total_price = total_price + int(item_new_prices[key]) * int(item_codes[key])
    return total_price




print(calculate_bag_total([ "ABC010", "DEF020", "ABC010" ], [ "ABC2P50", "ABC2P105" ]))
