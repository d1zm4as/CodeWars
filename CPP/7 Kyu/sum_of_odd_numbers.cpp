int ipow(int base, int exp){
    int result = 1;
    for (;;){
        if (exp & 1)result *= base;exp >>= 1;if (!exp)break;base *= base;}return result;}

long long rowSumOddNumbers(unsigned n){
  return ipow(n,3);
}