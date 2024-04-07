#include <stdbool.h>
#include <math.h>
bool is_prime(int x)
{
    if (x==2 || x == 3){
      return true;
    }
    if (x<2 || x%2==0){
      return false;
    }
    int lim = round(sqrt(x))+1;
    for (int i = 3; i <= lim;i+=2){
      if(x%i==0){
        return false;
      }
    }
  
  
    return true;
}

int soma(int numbers[], int tam){
  int total = 0;
  int i;
  for(i = 0;i<tam;i++){
    total+=numbers[i];
    
  }
  return total;
}


int minimumNumber(int numbers[], int count)
{
    int total = soma(numbers,count);
    int cont = 0;
    while(!is_prime(total)){
      cont++;
      total++;
    }
    return cont;
}