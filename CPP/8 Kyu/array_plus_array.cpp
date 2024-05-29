#include <vector>
#include <numeric>
int arrayPlusArray(std::vector<int> a, std::vector<int> b) {
  int soma1 = std::accumulate(a.begin(), a.end(), 0);
  int soma2 = std::accumulate(b.begin(), b.end(), 0);
  
  return soma1+soma2; // something went wrong
}