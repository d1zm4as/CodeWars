/* The first parameter argc will indicate
 how many additional arguments were passed to the function.
 All arguments will be of type int
*/

#include <stdarg.h>
int sum (int n, ...)
{ 
  
    int soma = 0;
   va_list ptr;
 
    // Initializing argument to the
    // list pointer
    va_start(ptr, n);
 
    for (int i = 0; i < n; i++)
 
        // Accessing current variable
        // and pointing to next one
        soma += va_arg(ptr, int);
 
    // Ending argument list traversal
    va_end(ptr);
    return soma;
}
