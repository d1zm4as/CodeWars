#include <stdio.h>
#include <stdint.h>
char *USD_to_CNY (long dollars, char *yuans)
{
  sprintf(yuans, "%.2Lf Chinese Yuan", (long double) dollars * 6.75);
	return yuans; // return it
}