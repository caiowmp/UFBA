# moedas: 50,25,10,5,1

n = int(input())

resto = n

moeda = 50
quociente = resto // moeda
print(quociente,"moeda(s) de",moeda)
resto = resto % moeda

moeda = 25
quociente = resto // moeda
print(quociente,"moeda(s) de",moeda)
resto = resto % moeda

moeda = 10
quociente = resto // moeda
print(quociente,"moeda(s) de",moeda)
resto = resto % moeda

moeda = 5
quociente = resto // moeda
print(quociente,"moeda(s) de",moeda)
resto = resto % moeda

moeda = 1
quociente = resto // moeda
print(quociente,"moeda(s) de",moeda)
resto = resto % moeda