#include <vector>
#include <numeric>
double calcAverage(const std::vector<int>& numbers){
  int tam = numbers.size();
  if(!tam){
    return 0;
  }
  double total = accumulate(begin(numbers), end(numbers), 0, std::plus<int>());
  return total/tam;
}