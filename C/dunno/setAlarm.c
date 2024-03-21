#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

bool set_alarm(bool employed, bool vacation) {

    if(employed==true&&vacation==false){return 0; }else{return 1;}

}


int main(){

    printf("%d\n",set_alarm(true, false));


    return 0;
}