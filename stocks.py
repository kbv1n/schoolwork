stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

totalprice = 0
numinput = 3
for i in range(numinput):
    userstock = str(input())
    if userstock in stocks:
       totalprice += stocks[userstock]
       
print(f'Total price: ${totalprice}')