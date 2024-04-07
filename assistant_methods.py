
def check_receipt(receipt, sample):
    if f'(==== {sample["bun"]} ====)\n' in receipt:
        if f'= {sample["filling_type"]} {sample["ingredient"]} =\n' in receipt:
            if f'Price: {sample["price"]}' in receipt:
                return "OK"

