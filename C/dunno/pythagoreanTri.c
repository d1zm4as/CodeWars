#include <stdbool.h>
//#include <stdlib.h>
#include <stdio.h>


bool pythagorean_triple(const unsigned sides[2]) {
    
    unsigned long a = sides[0]*sides[0],b = sides[1]*sides[1],c = sides[2]*sides[2]; 
    
    return a+b ==c ||c+a == b ||b+c ==a;   
}


int main(){
const unsigned sides[]= {3,4,6};
printf("%d\n",pythagorean_triple(sides));
return 0;
}
