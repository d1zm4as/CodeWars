#include <vector>
#include <bits/stdc++.h>
int maxSequence(const std::vector<int>& array){
  int best = 0, sum = 0;
  int tam =array.size();
  for (int k = 0; k < tam; k++) {
  sum = fmax(array[k],sum+array[k]);
  best = fmax(best,sum);
  }
  return best;
}