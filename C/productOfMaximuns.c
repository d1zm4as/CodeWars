#include <stdio.h>

void InsertionSort(int array[], int tam){
    
    for(int i = 1;i<tam;i++){
    int j = i;
    int temp = array[i];
    while(j>0&&array[j-1]>temp){
        array[j]=array[j-1];
    j--;
    }
    array[j] = temp;
}

}

int maxProduct (int numbers[], int numbers_size, int sub_size)
{
  InsertionSort(numbers, numbers_size);
  int produto = 1;
  int start = numbers_size-sub_size;  
  for(int i=start;i<numbers_size;i++){
    printf("%d ",numbers[i]);
    produto*=numbers[i];
  }
  printf("\n");
  printf("%d\n",produto);

  return 1 ;
}




int main(){
    //int array[] = {4,3,5}; 
    //int array[] = {10,8,7,9};
    //int array[] = {8,6,4,6};
//int array[] = {13,12,-27,-302,25,37,133,155,-14};
    //int array[] ={14,29,-28,39,-16,-48};
    int array[]= {-4,-27,-15,-6,-1};
    int tam= sizeof(array)/sizeof(array[0]);
    int sub_size = 2;
    maxProduct(array, tam,  sub_size);


    return 0 ;
}