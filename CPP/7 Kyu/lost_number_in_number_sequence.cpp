using namespace std;
#include <numeric>


int findDeletedNumber(list<int> startingList, list<int> mixedList)
{
   int a =  accumulate(startingList.begin(), startingList.end(), 0);
   int b =  accumulate(mixedList.begin(), mixedList.end(), 0);
  
  return a-b;

}