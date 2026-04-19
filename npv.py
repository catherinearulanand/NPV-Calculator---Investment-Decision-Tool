def calculate_npv(initial_investment, cash_flows, rate):
    npv = -initial_investment
    
    for t in range(len(cash_flows)):
        npv += cash_flows[t] / ((1 + rate) ** (t + 1))
    
    return npv

initial = float(input("Enter initial investment: "))

years = int(input("Enter number of years: "))

cash_flows = []
for i in range(years):
    cf = float(input(f"Enter cash flow for year {i+1}: "))
    cash_flows.append(cf)

rate = float(input("Enter discount rate (in decimal, e.g., 0.1 for 10%): "))

result = calculate_npv(initial, cash_flows, rate)

print("\nNPV:", result)

if result > 0:
    print("Good investment.")
else:
    print("Not worth it.")
