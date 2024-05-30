#include <string>

using namespace std;

int getCount(const string& s){
  int num_vowels = 0;
  //your code here
  int tam  = s.size();
  int cont = 0;
  for(size_t i = 0; i<tam; i++){
        
        if (s[i]=='a' || s[i]=='e' ||s[i]=='i' ||s[i]=='o' ||s[i]=='u' ||s[i]=='A' ||s[i]=='E' ||s[i]=='I' ||s[i]=='O' ||s[i]=='U'){
           cont++;
        }
    }
  return cont;
}