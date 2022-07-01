#include <iostream>
#include<string>
#define TAM 10

using namespace std;

void imprime_vetor(int vetor[TAM]){
  int i;

  for( i=0; i<TAM; i++){
    cout<<vetor[i]<<" ";
  }

  cout<<endl;
}

//Bubble sort Crescente.
void bubble_sort(int vetor[TAM]){
  int i, j , aux;

  for( i=0; i<TAM-1; i++){
    for( j = i + 1; j<TAM; j++){
      if(vetor[i] > vetor[j]){
        aux = vetor[j];
        vetor[j] = vetor[i];
        vetor[i] = aux;
      }
    }
  } 
}

int main() {
  int vetor[TAM] = {10,9,8,7,6,5,4,3,2,1};

  imprime_vetor(vetor);

  bubble_sort(vetor);

  imprime_vetor(vetor);


return 0;
}
