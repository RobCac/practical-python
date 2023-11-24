# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_count = 0
extra_payment_sum = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    payment_count += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if payment_count in range(extra_payment_start_month, extra_payment_end_month+1):
        total_paid = total_paid  + extra_payment_sum
        principal = principal - extra_payment_sum
    print(payment_count, total_paid, principal)
       

print('Total paid', total_paid)
print(f"Months {payment_count}")
