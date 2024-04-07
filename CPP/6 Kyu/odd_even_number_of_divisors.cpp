#include <string>
#include <cmath>
typedef long long ll;
bool is_prime(ll x)
{
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
  
std::string oddity(long long int n) {
  if (is_prime(n)){
    return "even";
  }
  int total = 1;
  for(int i= 2;i<=n;i++){
    if (n%i==0){
      total++;
    }
  }
  
  if(total%2==0){
    return "even";
  }
  
  return "odd";
}
  