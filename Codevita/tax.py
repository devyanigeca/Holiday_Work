s = list(map(int, input().strip().split(" ")))
t = list(map(int, input().strip().split(" ")))
rebate = int(input().strip())
tpaid = list(map(int, input().strip().split(" ")))


finalsalaries = []

taxlimits = []
for i in range( len(s)-1):
    diffslab = s[i+1] - s[i]
    max_tax = diffslab*t[i] / 100
    taxlimits.append(max_tax)

for tax_now in tpaid:
    aggtax = tax_now
    x1 = s[0]
    for i in range(len(taxlimits)):
        if aggtax < taxlimits[i]:
            x1 = (aggtax/(t[i]/100)) + s[i]
            aggtax = 0
            break
        else:
            x1 = s[i+1]
            aggtax -= taxlimits[i]

    if aggtax != 0:
        x1 = aggtax / (t[-1] / 100) + s[-1]

    finalsalaries.append(x1)


sum_salary = sum(finalsalaries) + len(finalsalaries)*rebate

print(int(sum_salary), end="")