#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>

int main(void) {
    int fd1[2], /* Pai vai escrever e Filho ler por esse file descriptor */
         fd2[2], /* Pai vai ler e o Filho escrever por esse file descriptor */
         turn=0; /* Vai definir o que cada um vai fazer (ler, escrever, aguardar...) */
    pid_t pid;   /* Armazena o pid, para o tratamento de pai e filho */

    /* Cria o pipe 1 */
    if(pipe(fd1)<0) {
        perror("pipe") ;
        return -1 ;
    }
    /* Cria o pipe 2 */
    if(pipe(fd2)<0) {
        perror("pipe") ;
        return -1 ;
    }

    /* Cria processo filho. */
    pid = fork();

    if(pid == -1) {
        perror("fork") ;
        return -1 ;
    }

    if(pid > 0) {    /* Processo pai*/
        int num[3],  /* Números que o processo pai lê*/
              x[2];    /* Resultado da equação, recebido pelo filho*/

        /* Fechando o descritor LEITURA no primeiro pipe. */
        close(fd1[0]);
        /* Fechando o descritor ESCRITA no segundo pipe. */
        close(fd2[1]);

        while(1)
            if(turn==0){ /* Pai vai escreever */
                printf("Insira o numero 'a': "); scanf("%d", &num[0]);
                printf("Insira o numero 'b': "); scanf("%d", &num[1]);
                printf("Insira o numero 'c': "); scanf("%d", &num[2]);

                write(fd1[1], num, sizeof(num)); /* Enviando o vetor de números pro filho */
                turn=1; /* Passa para o próximo passo, que é o pai ler a soma do filho */
            }

            if(turn==1){ /* Pai vai ler as raizes */
                read(fd2[0], &x, sizeof(x)); /* Pai leu o resultado das raizes e aramzenou no vetor x */
                printf("x1: %d\n\n", x[0]);
                printf("x2: %d\n\n", x[1]);
              
                turn=0;  /* Retorna pro passo anterior, pra começar tudo de novo */
            }


        close(fd2[0]);
        close(fd1[1]);

    } else {
        int numeros[3],
             raizes[2];

        /* Fechando o descritor ESCRITA no primeiro pipe. */
        close(fd1[1]);
        /* Fechando o descritor LEITURA no segundo pipe. */
        close(fd2[0]);

        while(1){
            if(turn==0){ /* Filho vai ler o vetor de numeros do pai */
                read(fd1[0], numeros, sizeof(numeros) ); /* Recebeu o vetor de inteiros do pai e colocou no vetor 'numeros' */
                turn=1;  /* Passa para o próximo passo, que é o filho calcular as raizes e escrever */
            }else

            if(turn==1){ /* Filho calcula as raíze e retorna pro pai */
              float bNeg = 0 - numeros[1];
              float bquad = numeros[1] * numeros[1];
              float ac4 = 4*numeros[0] * numeros[2];
              float delta = bquad - ac4;
              float sqrdelta = sqrt(delta);
              float a2 = 2*numeros[0];
              
                raizes[0] = (bNeg + sqrdelta)/a2;
                raizes[1] = (bNeg - sqrdelta)/a2;

                write(fd2[1], &raizes, sizeof(raizes)); /* Envia a soma, qúe está na variável 'soma', para o pai */
                turn=0; /* Volta para o passo anterior, que é esperar vetor de inteiros do pai */
            }
        }

        close(fd2[1]);
        close(fd1[0]);
    }

    return 0 ;
}