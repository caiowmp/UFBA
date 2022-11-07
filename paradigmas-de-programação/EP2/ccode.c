/* Exercicio EP2 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// funcao f1
// uma que declara um array grande estaticamente
void f1() { static int lista[10000]; }

// funcao f2
// uma que declara o mesmo array na pilha (semi-estáticas ou dinâmicas de pilha)
void f2()
{
    int array[10000];
    return;
}

// funcao f3
// uma que cria o mesmo array na heap (dinâmicas)
void f3()
{
    int *array;
    array = (int *)malloc(10000 * sizeof(int));
}

// funcao main

int main()
{
    double time_spent = 0.0;
    clock_t begin = clock();

    for (int i = 0; i < 100000; i++)
    {
        f1();
    }

    clock_t end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;

    printf("The elapsed time is %f seconds\n", time_spent);
    begin = clock();

    for (int i = 0; i < 100000; i++)
    {
        f2();
    }

    end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;

    printf("The elapsed time is %f seconds\n", time_spent);
    begin = clock();

    for (int i = 0; i < 100000; i++)
    {
        f3();
    }

    end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;

    printf("The elapsed time is %f seconds\n", time_spent);
}