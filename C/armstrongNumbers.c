#include <stdio.h>


int tam(int num){int cont = 0;while(num>0){int mod = num%10; cont+=1;num=num/10; }return cont;}
int ipow(int base, int exp){int result = 1;for (;;){if (exp & 1)result *= base;exp >>= 1;if (!exp)break;base *= base;}return result;}

int main(){
    int num;
    
    //scanf("%d",&num);
    num = 153;
    int pod = tam(num);
    int soma = 0;
    while(num > 0) //do till num greater than  0
    {
        int mod = num % 10;  //split last digit from number
        
        soma += ipow(mod,pod);    
        num = num / 10;    //divide num by 10. num /= 10 also a valid one 
    }
    printf("%d\n",soma);
    if(soma==num){return 0;}else{return 1;}
    return 0;
}