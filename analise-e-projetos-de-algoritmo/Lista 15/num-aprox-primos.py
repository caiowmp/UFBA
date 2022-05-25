from cmath import log
import cmath

n = int(input())

p = n/log(n)

m = 1.25506 * p

print('%.1f' % p.real,"",end='')
print('%.1f' % m.real)