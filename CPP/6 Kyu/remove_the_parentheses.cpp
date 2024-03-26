#include <string>
using namespace std;
string remove_parentheses(const string &str)
{
    string  copy = "";
  
    int cont = 0;
    
    for(auto x:str){
      if (x!= '(' && cont==0){
        copy+=x;
        
      }else if(x=='('){
        cont+=1;
        
      }else if(x == ')'){
        cont-=1;
      }
    }
    return copy;
}