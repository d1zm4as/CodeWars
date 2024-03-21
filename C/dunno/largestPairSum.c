#include <stddef.h>
#include <stdio.h>
#include <limits.h>

long long largest_pair_sum (size_t tam, const int array[])
{
    long long maior = LONG_MIN;
    long long sec_maior = LONG_MIN;

    for(size_t i=0;i<tam;i++){
        if(array[i]>maior){
            sec_maior = maior;
            maior = array[i];
        }else if(array[i]>sec_maior){
            sec_maior = array[i];
        }
        
    }
    


  return maior+sec_maior;

//     long long highest = LLONG_MIN, next_highest = LLONG_MIN;

//   for (size_t i = 0; i < tam; i++) {
//     if (array[i] > highest) {
//       next_highest = highest;
//       highest = array[i];
//     } else if (array[i] > next_highest) {
//       next_highest = array[i];
//     }
//   }
//   return highest + next_highest;

} 

// [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
// [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
// {-100, -29, -24, -19, 19}->0
//{97, -63, 75, -8, -49, -88, 37, 51, -68, -18, 72, 0, 22, 9, -81}->172
int main(){


    //const int array[]= {10,14, 2, 23, 19};
    //const int array[]= {99,2, 2, 23, 19};
    //const int array[] = {-100, -29, -24, -19, 19};
    //const int array[] = {3,3};
    const int array[] = {97, -63, 75, -8, -49, -88, 37, 51, -68, -18, 72, 0, 22, 9, -81};
    size_t tam = sizeof(array)/sizeof(array[0]);
    printf("%Ld\n",largest_pair_sum(tam, array));
    return 0;
}