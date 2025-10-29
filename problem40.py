
a = ""
for x in range (1,190001):
    a += str(x)


sol = int(a[0])*int(a[9])*int(a[99])*int(a[999])*int(a[9999])*int(a[99999])*int(a[999999])
print(sol)