#include <stdio.h>

int tam(int a){
    if(a>0 && a<=10){
        return 10;
    }
    else if(a>10 && a<=100){
        return 100;
    }  else{
        return 1000;
    }

}

int check(int a){
    if((a*a )%tam(a)==a){
        printf("Automorphic\n");
    }else{
        // return 1;
        printf("Not!!\n");

    }

    return 0;
}


int main(){

    
    //int a = 625;

    check(1);  
    check(3);  
    check(6);  
    check(9);  
    check(25);  
    check(13);  
    check(76);  
    check(95);  
    check(625);
    check(225);
    check(425);
    check(399);





    return  0;
}























