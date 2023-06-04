#include <ctype.h>

int same_case(char a, char b)
{
    if (!isalpha(a) || !isalpha(b))
        return -1;
    return !isupper(a) == !isupper(b);
}



int main(){





    return 0;
}