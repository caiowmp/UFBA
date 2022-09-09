## Retângulo com construtor

Perceba que, se você consultar a área de um retângulo sem antes definir suas medidas, ocorre um erro. Exemplo:

```
r = Retangulo()
print(r.area())
# Resultado: "AttributeError: 'Retangulo' object has no attribute 'base'"
```

Para evitar esse problema, você deve criar um construtor/inicializador.

Copie sua solução do exercício anterior e cole aqui, fazendo uma modificação: defina a classe `Retangulo` de forma que, para instanciar um objeto, é necessário informar base e altura.