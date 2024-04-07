#include <numeric>
using namespace std; 
bool isPrime(int x) {
  if (x==2 || x == 3){
      return true;
    }
    if (x<2 || x%2==0){
      return false;
    }
    int lim = round(sqrt(x))+1;
    for (int i = 3; i <= lim;i+=2){
      if(x%i==0){
        return false;
      }
    }
    return true;
}

int minimumNumber (vector <int> numbers )
{
  int total = accumulate(begin(numbers), end(numbers), 0, plus<int>());
  int cont = 0;
  while(!isPrime(total)){
    total++;
    cont++;
    }
  return cont;

}