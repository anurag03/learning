def insert_bills():
    bills = [10000, 5000, 2000, 1000, 0]
    bill = int(input("Select Bill"))
    if bill not in bills:
        bill = int(input("Select Bill"))
    bill_quantity = int(input("No of Bills"))
    bill_total = bill*bill_quantity
    return bill_total

def insert_coin():
    coins = [500, 100, 50, 10, 5, 1, 0]
    coin = int((input("Select Coin")))
    if coin not in coins:
        coin = int((input("Select Coin")))    
    coin_quantity = int((input("No of Coins")))
    return coin*coin_quantity

def return_calculation(payment_due, total_paied):
    bills = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    return_total = total_paied - payment_due
    print(return_total)
    for bill in bills:
        if return_total >= bill:
            return_bill = int(return_total/bill)
            print(bill)
            print(return_bill)
            return_total = return_total - (bill*return_bill)
            
payment_due = int(input("Payment Due"))
collected_bill = insert_bills()
collected_coin = insert_coin()
total_paid = collected_bill + collected_coin
return_calculation(payment_due, total_paid)


