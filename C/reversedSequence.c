#include <stdlib.h>
#include <stdio.h>


int main(){

    int num =5;

    int rev[num];
    int cont = 0;
    for(int i = num; i>0;i--){
        rev[cont] = i;

        cont++;
    }
    for(int i =0; i<num;i++){
        printf("%d ",rev[i]);

    }

    return 0;
}