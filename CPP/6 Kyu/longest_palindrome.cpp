#include <algorithm>
int longest_palindrome(const std::string &s)
{
    int maxlen = 0;
    for ( int i = 0; i < s.size(); ++i )
    for ( int j = 0; j < s.size(); ++j )
    {
      std::string sub = s.substr(i, s.size()-j);
      std::string rev = sub;
      std::reverse ( rev.begin(), rev.end());
      
      if ( sub == rev )
        maxlen = sub.size() > maxlen ? sub.size() : maxlen;
    }
    
    
    return maxlen;
}