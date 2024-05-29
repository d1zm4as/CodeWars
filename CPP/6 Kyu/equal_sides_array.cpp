#include <vector>
#include <numeric>
using namespace std;
// accumulate(nums.begin(), nums.end(), 0
int dunno(const vector<int>numbers, int start, int finish){
  int soma = 0;
  while( start<finish){
    soma+=numbers[start];
    start++;
  }
  return soma;
}
int find_even_index (const vector <int> numbers) {
  int tam = numbers.size();
  for(int i = 0;i<tam;i++){
    if (dunno(numbers,0,i) == dunno(numbers,i+1,tam)) {
      return i;
      
    }
  
  }
  return -1;
}
//     int left_sum = std::accumulate(numbers.begin(), numbers.begin() + index, 0);
// melhor forma de somar slices