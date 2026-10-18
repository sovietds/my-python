monthly_invest = 1000 #每月定投金额
annual_return = 0.08 #年化收益率8%
years = 5 
months = years * 12 #60个月
monthly_rate = annual_return / 12 #月利率
month_list = []
invest_list = []
balance_list = []
balance = 0 #账户从0开始
for month in range(1,months+1):
    balance = balance * (1 + monthly_rate) #老钱生息
    balance = balance + monthly_invest     #投入新钱
    month_list.append(month)
    invest_list.append(monthly_invest)
    balance_list.append(round(balance,2))
print(balance_list) #60个月余额
print(balance_list[0]) #第1个月余额
print(balance_list[11]) #第12个月余额
print(balance_list[-1]) #第60个月余额（最终）
for value in balance_list[-6:]: #遍历最后6个月余额
    print(value)
total_invest = sum(invest_list) #本金总合计
final_value = balance_list[-1] #期末总额
total_profit = final_value - total_invest #收益
return_rate = total_profit / total_invest * 100 #收益率
print(total_invest,final_value,total_profit,round(return_rate,2))