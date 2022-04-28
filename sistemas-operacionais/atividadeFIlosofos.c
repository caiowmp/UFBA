#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

#define N 5
#define pensando 2
#define comFome 1
#define comendo 0
#define esquerda (i + 4) % N
#define direita (i + 1) % N

int estado[N];
int phil[N] = { 0, 1, 2, 3, 4 };

sem_t mutex;
sem_t S[N];

void test(int i)
{
	if (estado[i] == comFome
		&& estado[esquerda] != comendo
		&& estado[direita] != comendo) {
		// estado comendo
		estado[i] = comendo;

		sleep(2);

		printf("Filosofo %d pegou o garfo %d e %d\n",
					i + 1, esquerda + 1, i + 1);

		printf("Filosofo %d está comendo\n", i + 1);

		sem_post(&S[i]);
	}
}

// pega os garfos
void take_fork(int i)
{

	sem_wait(&mutex);

	// estado recebe comFome
	estado[i] = comFome;

	printf("Filosofo %d está comFome\n", i + 1);

	// come se os filosofos ao lado não estão comendo
	test(i);

	sem_post(&mutex);

	// se não poder comer, espera ser sinalizado que pode
	sem_wait(&S[i]);

	sleep(1);
}

// coloca os garfos na mesa
void put_fork(int i)
{

	sem_wait(&mutex);

	// estado recebe pensando
	estado[i] = pensando;

	printf("Filosofo %d colocando garfo %d e %d na mesa\n",
		i + 1, esquerda + 1, i + 1);
	printf("Filosofo %d está pensando\n", i + 1);

	test(esquerda);
	test(direita);

	sem_post(&mutex);
}

void* philosopher(void* num)
{

	while (1) {

		int* i = num;

		sleep(1);

		take_fork(*i);

		sleep(0);

		put_fork(*i);
	}
}

int main()
{

	int i;
	pthread_t thread_id[N];

	// inicializando semáforos 
	sem_init(&mutex, 0, 1);

	for (i = 0; i < N; i++)

		sem_init(&S[i], 0, 0);

	for (i = 0; i < N; i++) {

		// cria um processo filósofo
		pthread_create(&thread_id[i], NULL,
					philosopher, &phil[i]);

		printf("Filosofo %d está pensando\n", i + 1);
	}

	for (i = 0; i < N; i++)

		pthread_join(thread_id[i], NULL);
}

