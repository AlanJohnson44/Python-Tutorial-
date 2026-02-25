print("Income Tax Calculator (FY 2024-25)")
income = float(input("Enter your Total Annual Income (in Rupees): "))
tax = 0.0
if income <= 300000:
    tax = 0.0
elif income <= 700000:
    tax = (income - 300000) * 0.05
elif income <= 1000000:
    tax = 20000 + (income - 700000) * 0.10
elif income <= 1200000:
    tax = 50000 + (income - 1000000) * 0.15
elif income <= 1500000:
    tax = 80000 + (income - 1200000) * 0.20
else:
    tax = 140000 + (income - 1500000) * 0.30
if income <= 700000:
    tax = 0.0
print("Total Income:   ₹", income)
print("Tax Payable:    ₹", tax)
