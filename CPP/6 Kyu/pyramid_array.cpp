#include <vector>
#include <cstdlib>

std::vector<int> lol(std::size_t n){
  
  std::vector<int> lista = {};
  for(size_t i = 1; i<=n;i++){
      lista.push_back(1);
    }
  return lista;
}

std::vector<std::vector<int>> pyramid(std::size_t n) {
  if(n==0){
    return {};
  }
  

  std::vector<std::vector<int>>lista = {};
    for(size_t i = 1; i<=n;i++){
      lista.push_back(lol(i));
    }
    return lista;
  
}