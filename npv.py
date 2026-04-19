def calculate_npv(initial_investment, cash_flows, rate):
    npv = -initial_investment
    
    for t in range(len(cash_flows)):
        npv += cash_flows[t] / ((1 + rate) ** (t + 1))
    
    return npv

def get_investment_data(name):
    print(f"\n--- Enter details for {name} ---")
    
    initial = float(input("Initial investment: "))
    years = int(input("Number of years: "))
    
    cash_flows = []
    for i in range(years):
        cf = float(input(f"Cash flow for year {i+1}: "))
        cash_flows.append(cf)
    
    rate = float(input("Discount rate (e.g., 0.1 for 10%): "))
    
    return initial, cash_flows, rate
 
initial_A, cash_A, rate_A = get_investment_data("Investment A")
initial_B, cash_B, rate_B = get_investment_data("Investment B")

npv_A = calculate_npv(initial_A, cash_A, rate_A)
npv_B = calculate_npv(initial_B, cash_B, rate_B)

print("\n--- Results ---")
print(f"NPV of Investment A: {npv_A}")
print(f"NPV of Investment B: {npv_B}")
 
if npv_A > npv_B:
    print("Investment A is better")
elif npv_B > npv_A:
    print("Investment B is better")
else:
    print("Both investments are equally good")
