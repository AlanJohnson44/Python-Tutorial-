investment = float(input("Enter the initial investment amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
years = int(input("Enter the number of years: "))

print(f"\n{'Year':<8}{'Amount'}")

amount = investment

for year in range(1, years + 1):
    amount = amount + (amount * (rate / 100))
    print(f"{year:<8}{amount:.2f}")
