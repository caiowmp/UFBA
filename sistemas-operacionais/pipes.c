#include <sys/sem.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
	int fd_1[2], fd_2[2], fd_3[2], fd_4[2], fd_5[2];
	pid_t son1, son2, son3, son4;
	
	pipe(fd_1);
	pipe(fd_2);
	pipe(fd_3);

	//Cria o primeiro processo
	if(son1 = fork() == -1)
	{
		perror("fork");
		exit(1);
	}

	//Lê o valor de a
	if(son1 == 0)
	{
		float a;
		
		printf("Processo %d \n",getpid());
		printf("Digite o valor de 'a' da equação\n");
		//lê o valor de A
		scanf("%f",a);
		//fecha a parte de leitura
		close(fd_1[0]);
		//escreve a no pipe fd_1
		write(fd_1[1], &a,(sizeof(float)));
		
		exit(0);
	}

	//Cria o segundo processo
	if(son2 = fork() == -1)
	{
		perror("fork");
		exit(1);
	}

	//Lê o valor de b
	if(son2 == 0)
	{
		float b;
	
		printf("Processo %d \n",getpid());
		printf("Digite o valor de 'b' da equação\n");
		//lê o valor de B
		scanf("%f",b);
		//fecha a parte de leitura
		close(fd_2[0]);
		//escreve b no pipe fd_2
		write(fd_2[1], &b,(sizeof(float)));
		
		exit(0);
	}

	//Cria o terceiro processo
	if(son3 = fork() == -1)
	{
		perror("fork");
		exit(1);
	}

	//Lê o valor de c
	if(son3 == 0)
	{
		float c;
	
		printf("Processo %d \n",getpid());
		printf("Digite o valor de 'c' da equação\n");
		//lê o valor de C
		scanf("%f",c);
		//fecha a parte de leitura
		close(fd_3[0]);
		//escreve c no pipe fd_3
		write(fd_3[1], &c,(sizeof(float)));
		
		exit(0);
	}

	//Cria o quarto processo
	if(son4 = fork() == -1)
	{
		perror("fork");
		exit(1);
	}

	//Calcula os valores de de x1 e x2 e imprime na tela
	if(son4 == 0)
	{
		float a, b, c, x1, x2;
		
		printf("Processo %d\nCalculando as raízes da equação\n",getpid());
		
		//recebe a
		//fecha a parte de escrita
		close(fd_1[1]);
		//lê o valor do buffer
		read(fd_1[0], &a, (sizeof(float)));
		
		//recebe b
		//fecha a parte de escrita
		close(fd_2[1]);
		//lê o valor do buffer
		read(fd_2[0], &b, (sizeof(float)));

		//recebe c
		//fecha a parte de escrita
		close(fd_3[1]);
		//lê o valor do buffer
		read(fd_3[0], &c, (sizeof(float)));
		
		printf("As raizes da equação são: x1 = %f e x2 = %f",x1, x2);
		exit(0);
	}
	
	return 0;
}


