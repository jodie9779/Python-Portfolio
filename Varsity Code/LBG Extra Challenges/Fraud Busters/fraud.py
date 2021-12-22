class ClassName:

    def sorter(self, balance1, balance2):
        import re
        import statistics
        if len(balance1) < 3 or len(balance2) < 3:
            return (-1.0)
        account1_match = bool(re.match("[0-9]{8}", balance1[0]))
        account2_match = bool(re.match("[0-9]{8}", balance2[0]))
        if account1_match is False or account2_match is False:
            return (-1.0)
        sort1_match = bool(re.match("[0-9]{2}-[0-9]{2}-[0-9]{2}", balance1[1]))
        sort1_match2 = bool(re.match("[0-9]{6}", balance1[1]))
        sort2_match1 = bool(re.match("[0-9]{2}-[0-9]{2}-[0-9]{2}", balance1[1]))
        sort2_match2 = bool(re.match("[0-9]{6}", balance1[1]))
        if sort1_match is False and sort2_match2 is False:
            return (-1.0)
        if sort2_match1 is False and sort2_match2 is False:
            return (-1.0)
        balance1_transactions = balance1[2:]
        valid_transactions = list()
        balance2_transactions = balance2[2:]
        def validity_check(trans):
            decimalcheck1 = bool(re.match("^.+\.[0-9]{2}$", trans))
            decimalcheck2 = bool(re.match("^£.+\.[0-9]{2}$", trans))
            if decimalcheck1 is False and decimalcheck2 is False:
                return
            startcheck1 = bool(re.match("£0+[0-9]+\.[0-9]{2}", trans))
            startcheck2 = bool(re.match("^0+[0-9]+\.[0-9]{2}", trans))
            if startcheck1 is True or startcheck2 is True:
                return
            return True
        for transaction in balance1_transactions:
            if validity_check(transaction) is True:
                pound_check = bool(re.match("^£", transaction))
                if pound_check is True:
                    numberonly = transaction[1:]
                    valid_transactions.append(float(numberonly))
                else:
                    valid_transactions.append(float(transaction))
            else:
                continue
        for transaction in balance2_transactions:
            if validity_check(transaction) is True:
                pound_check = bool(re.match("^£", transaction))
                if pound_check is True:
                    numberonly = transaction[1:]
                    valid_transactions.append(float(numberonly))
                else:
                    valid_transactions.append(float(transaction))
            else:
                continue
        if len(valid_transactions) == 0:
            return (-1.0)
        median = statistics.median(valid_transactions)
        return median

