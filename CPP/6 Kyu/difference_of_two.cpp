#include <utility>
#include <vector>
using namespace std;
vector<pair<int, int>> twos_difference(const vector<int> &vec) {
  vector<pair<int,int>> lista = {};
  for (auto x : vec) {
    for(auto y: vec){
      if((y-x)==2){
        lista.push_back({x,y});
      }
    }
  
  }

  sort(lista.begin(), lista.end());

return lista;

}