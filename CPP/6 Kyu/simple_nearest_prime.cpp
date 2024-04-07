#include <cmath>
bool isPrime(long long x) {
  if (x==2 || x == 3){
      return true;
    }
    if (x<2 || x%2==0){
      return false;
    }
    int lim = round(sqrt(x))+1;
    for (long long i = 3; i <= lim;i+=2){
      if(x%i==0){
        return false;
      }
    }
    return true;
}



long long solve(long long n){
    if(isPrime(n)){
      return n;
}
    long long prox = n+1;
    long long ant = n-1;
    while(1){
      if(isPrime(ant)){
            return ant;
      }     
      if(isPrime(prox)){
          return prox;
      }
      
      ant-=1;
      prox+=1;
    
    }
}