def process_transactions(transactions):
    balance = 0
    for transaction in transactions:
        action, amount = transaction.split()
        amount = int(amount)
        if action == 'D':
            balance += amount
        elif action == 'W':
            balance -= amount
    return balance
transactions = []
print("Nhập nhật ký giao dịch (nhập 'end' để kết thúc):")
while True:
    transaction = input()
    if transaction.lower() == 'end':
        break
    transactions.append(transaction)
final_balance = process_transactions(transactions)
print("Số tiền thực của tài khoản là:")
print(final_balance)
