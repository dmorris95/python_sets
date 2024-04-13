#Task 1

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

#changing the list to set removes all duplicates
def set_change(cust_ids):
    customer_set = set(cust_ids)
    print(customer_set)

set_change(customer_ids)