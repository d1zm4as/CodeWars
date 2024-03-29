#include <vector>

int sum(std::vector<int> nums) {
  int soma, i;
  soma = 0;
  
  for (auto x: nums){
    soma+=x;
  }
  return soma;
  
}

// #include <vector>
// #include <numeric>

// int sum(std::vector<int> nums) {
//   return std::accumulate(nums.begin(), nums.end(), 0);
// }