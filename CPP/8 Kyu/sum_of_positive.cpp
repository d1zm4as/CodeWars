#include <vector>
int positive_sum (const std::vector<int> arr){
  // Your code here
  int tam = arr.size();
  if (tam ==0){
    return 0;
  }
  
  int total = 0;
  for(size_t i = 0; i< tam; i++){
    if(arr[i]>=0){
      total+=arr[i];
    }
  }
  return total;



}