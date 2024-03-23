#include <string>
using namespace std;
string removeExclamationMarks(string s){
  string copy = ""; 
  int tam = s.length();
  for(int i = 0; i<tam; i++){
    if(s[i] != '!'){
        copy+=s[i];
    }
  }
  
  return copy;
}