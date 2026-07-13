transaction_count = 0
def process_txn_():
    global transaction_count
    transaction_count += 1
    print(f"transaction processed. Count: {transaction_count}")
print(f"initial count: {transaction_count}")
process_txn_()
process_txn_()
print(f"Final count outside function: {transaction_count}")