familiares,gudePrimeir = map(int,input().split())
total = gudePrimeir

for i in range(familiares):
    total = total*2

print(total-gudePrimeir)
