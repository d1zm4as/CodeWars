#include <cmath>
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



unsigned int oddNotPrime(unsigned int n){
  int total = 0;
  int i;
  for(i = 1; i<=n;i++){
    if(!isPrime(i) && i%2!=0){
      total++;
    }
  }
  return total;
}