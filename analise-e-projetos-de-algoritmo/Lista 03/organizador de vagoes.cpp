#include <iostream>

using namespace std;

int main()
{

    int testes;

    cin >> testes;

    for(int i = 0; i< testes; i++)
    {

        int tamanho;

        cin >> tamanho;

        int vagoes[tamanho];

        int swaps = 0;

        for(int j = 0; j< tamanho; j++)
        {

            cin >> vagoes[j];

        }

        int aux;

        for(int i=0; i<tamanho-1; i++){
            for(int j = i + 1; j<tamanho; j++){
                if(vagoes[i] > vagoes[j]){
                    aux = vagoes[j];
                    vagoes[j] = vagoes[i];
                    vagoes[i] = aux;
                    swaps++;
                }
            }
        }

        cout << "Optimal train swapping takes " << swaps << " swaps." << endl;
    }

}