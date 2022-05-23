valor = int(input())
notas = [1,2,5,10,20,50,100]
#subproblemas => f(n) = f(n-1) + f(n-2) + f(n-5) + f(n-10) + f(n-20) + f(n-50) + f(n-100)

#forma ingênua
def ingenua(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ingenua(n-1)+ingenua(n-2)+ingenua(n-5)+ingenua(n-10)+ingenua(n-20)+ingenua(n-50)+ingenua(n-100)

#forma com programação dinâmica top down
memo = {0:0,1:1}
def funcao_pd(n):
    if n < 0:
        return 0
    elif n in memo:
        return memo[n]
    else:
        memo[n] = funcao_pd(n-1)+funcao_pd(n-2)+funcao_pd(n-5)+funcao_pd(n-10)+funcao_pd(n-20)+funcao_pd(n-50)+funcao_pd(n-100)
        return memo[n]

print(funcao_pd(valor))

#qual a complexidade desse algoritmo ?