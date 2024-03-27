#include <string>
using namespace std;
string sortMyString(const string &s)
{
    // your code here
  
    string copy1 = "";
    string copy2 = "";
  
    for(unsigned long i = 0; i<s.size();i++){
      if(i%2==0){
        copy1+=s[i];
      }else{
        copy2+=s[i];
        
      }
    }
  
  
    return copy1+ " "+copy2;
}