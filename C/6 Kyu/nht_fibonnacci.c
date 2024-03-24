typedef unsigned long long ull;

ull nth_fib(int n) {

   ull a= 0, b=1;
    while(--n)
      b = a+(a=b);
    return a;

}

int main(){

  printf("%d\n",24/10);


  return 0;
}