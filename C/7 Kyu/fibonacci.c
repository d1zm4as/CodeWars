int fib(int n)
{
  int a=0, b=1;
  while(--n)
    b = a + (a=b);
  return b;
}