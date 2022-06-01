altura = int(input())

vetor = ['>'] * altura

for i in range(1,altura+1,1):
    vetor[-i] = '#'
    print(*vetor,sep="") 