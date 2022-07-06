# Depósito de arquivo com replicação - trabalho-avaliativo-mata59

Repositório para controle de versões do trabalho avaliativo da disciplina MATA59 (Semestre 2022.1)

## Sobre

Esse trabalho é uma implementação de um **Depósito de arquivo com replicação**.

Temos basicamente três tipos de dispositivos:

1. **Client** - dispositivo que requisita e envia arquivos dos/para servers
2. **Server** - responsável por armazenar e prover arquivos para o client
3. **Hub** - responsável pela interação entre client e os servers

## Operações

O funcionamento básico consiste em dois modos:
	
1. **Modo de Depósito** - o client informa ao hub que arquivo local deseja salvar nos servers, informando também o nível de tolerância a falhas desejado, ou seja, quantos servers devem ter uma cópia do arquivo.
2. **Modo de Recuperação** - o client informa ao hub que arquivo ele deseja resgatar dos servers.

## Contexto

Dispositivos no contexto desse trabalho foi abstraído para locais distintos dentro do mesmo dispositivo. Por isso o nome do Hub é sempre o mesmo: 'localhost'. O local reservado para os servers está situado na pasta server_folders. Também temos as pasta local_folders, onde armazenamos os arquivos locais do client.

## Execução

Para executar, é necessário iniciar diferentes processos em terminais separados.

1. Inicie o código tcphub.py, que ficará ouvindo quaisquer requisições do client na porta 12000 e dos servers na porta 12001 para se conectarem a eles.
2. Inicie os servers executando diferentes processos do mesmo código tcpserver.py. A princípio, escolhemos números de porta a partir de 13000.
3. Inicie o client executando o código tcpclient.py.

Para executar cada um dos arquivos, basta fazer:

```python3 <nome_arquivo.py>```

## Links Úteis

O link do vídeo da apresentação desse trabalho está disponível em: https://www.youtube.com/watch?v=I90gDeEUy4A

O link da documentação desse trabalho está no link: https://lucaargolo.github.io/trabalho-avaliativo-mata59-docs

## Integrantes da Equipe

* Caio Miranda Pereira
* Caio Silva Pontes
* Luca Assis Argolo
* Vítor Alves Barbosa
