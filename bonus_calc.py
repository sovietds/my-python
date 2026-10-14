monthly = float(input("月薪："))
months = float(input("计发月数："))
perf = input("绩效A/B/C：").strip().upper()
years = float(input("入职年限："))
base_bouns = monthly * months
if perf == "A" and years >= 1:
   perf_bouns = monthly * 2
elif perf == "B" and years >= 1:
   perf_bouns = monthly * 1
else:
   perf_bouns = 0
total = base_bouns + perf_bouns
if total <= 50000:
   tax = total * 0.1
elif total >= 50000:
   tax = 50000 * 0.1 + (total - 50000) * 0.15
after_tax = total - tax
print(f"税前工资总额{total}元")
print(f"税额{tax}元")
print(f"税后工资总额{after_tax}元")
print(total > 100000)
print(not perf == "C" and perf_bouns > 0)
