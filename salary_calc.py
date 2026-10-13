income = float(input("月工资："))
year_income = income * 12
estimated_tax = year_income * 0.10
take_home = year_income - estimated_tax
print(f"年收入：{year_income}元")
print(f"估算个税：{estimated_tax}元")
print(f"一年到手：{take_home}元")
