#include <string>
#include <vector>
#include <cstdio>
std::string likes(const std::vector<std::string> &names)
{
    int tam = names.size();
    
    char buffer[1000];
    
    if(tam == 1){
      
      sprintf(buffer, "%s likes this", names[0].c_str());
      return buffer;
    }
    if(tam == 2){
      
      sprintf(buffer, "%s and %s like this", names[0].c_str(),names[1].c_str());
      return buffer;
    }
    if(tam == 3){
      sprintf(buffer, "%s, %s and %s like this", names[0].c_str(),names[1].c_str(),names[2].c_str());
      return buffer;
    }
    
    if (tam >= 4){
     
      sprintf(buffer, "%s, %s and %d others like this", names[0].c_str(),names[1].c_str(),tam-2);
      return buffer;
    }
  
  
  return "no one likes this";
}