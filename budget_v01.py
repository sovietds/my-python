sales_volume=float(input("预计销售件数(件):"))
unit_price=float(input("预计单价（元）："))
unit_cost=float(input("单位变动成本(元):"))
fixed_cost=float(input("固定费用(元):"))
revenue=sales_volume*unit_price
variable_cost=sales_volume*unit_cost
total_cost=variable_cost+fixed_cost
profit=revenue-total_cost
gross_margin=profit/revenue*100
print(f"{"="*30}\n【年度预算结果】\n{"="*30}")
print("预算收入:",round(revenue,2))
print("变动成本:",round(variable_cost,2))
print("固定成本:",round(fixed_cost,2))
print("预算利润:",round(profit,2))
print("预算利润率:",str(round(gross_margin,1))+"%")

