#include <stdio.h>

int min(int* array, int tam){int menor = array[0];for(int i=0;i<tam;i++){if(array[i]<menor){menor = array[i];}} return menor;}

int max(int* array, int tam){int maior = array[0];for(int i=0;i<tam;i++){if(array[i]>maior){maior = array[i];}} return maior;}




int main(){

    int array []= {-52, 56, 30, 29, -54, 0, -110};
    int tam = sizeof(array)/sizeof(array[0]);
    printf("%d\n",min(array,tam));
    
    printf("%d\n",max(array,tam));
    return 0;
}
