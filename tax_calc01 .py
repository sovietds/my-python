a = float(input("应发工资："))
b =  float(input("五险一金："))
c = float(input("专项附加扣除："))
f = float(input("个税起征点："))
d = a - b - c - f #应纳税所得额
if d <= 0:
    tax = 0
elif d <= 3000:
    tax = d * 0.03
elif d <= 12000:
    tax = d * 0.1 - 210
elif d <= 25000:
    tax = d * 0.2 - 1410
elif d <= 35000:
    tax = d * 0.25 - 2660
elif d <= 55000:
    tax = d * 0.3 - 4410
elif d <= 80000:
    tax = d * 0.35 - 7160
else:
    tax = d * 0.45 - 15160
e = d + f + c - tax #税后收入
print(f"{"="*8}月度个税计算器{"="*8}")
print(f"应付工资：{a:,.2f}元")
print(f"减：个税起征点：{f:,.2f}元")
print(f"减：五险一金：{b:,.2f}元")
print(f"减：专项附加扣除：{c:,.2f}元")
print(f"减：个人所得税：{tax:,.2f}元")
print(f"到手工资：{e:,.2f}元")
