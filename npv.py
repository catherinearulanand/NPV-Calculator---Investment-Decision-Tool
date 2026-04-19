def calculate_npv(initial_investment, cash_flows, rate):
    npv = -initial_investment
    
    for t in range(len(cash_flows)):
        npv += cash_flows[t] / ((1 + rate) ** (t + 1))
    
    return npv

initial = 100000  # ₹1 lakh investment
returns = [30000, 30000, 30000, 30000, 30000]  # 5 years
rate = 0.10  # 10%

result = calculate_npv(initial, returns, rate)

print("NPV:", result)

if result > 0:
    print("Good investment")
else:
    print("Not worth it")
