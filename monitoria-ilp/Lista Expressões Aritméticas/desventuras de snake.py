
entrada = input().split()

Q1,Q2,Q3 = entrada
Q1 = int(Q1)
Q2 = int(Q2)
Q3 = int(Q3)

resultado = Q1 + Q2 + Q3

#print(resultado)

entrada = input().split()

E1,E2,E3 = entrada
E1 = int(E1)
E2 = int(E2)
E3 = int(E3)

# 3* pois o ovo envenado explode
resultado = resultado - (3*(E1+E2+E3))

print(resultado)