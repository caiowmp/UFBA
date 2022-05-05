#subproblemas => funcao_ingenua(n-1) + funcao_ingenua(n-3) + funcao_ingenua(n-4) = funcao_ingenua(n)

#forma ingênua
def funcao_ingenua(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 3
    elif n == 4:
        return 4
    else:
        return funcao_ingenua(n-1) + funcao_ingenua(n-3) + funcao_ingenua(n-4)

#forma com programação dinâmica top down
memo = {1:1,2:1,3:3,4:4}
def funcao_pd(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = funcao_pd(n-1) + funcao_pd(n-3) + funcao_pd(n-4)
        return memo[n]

n = int(input())
print(funcao_pd(n))

#qual a complexidade desse algoritmo ?