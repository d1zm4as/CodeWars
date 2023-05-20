#include <stdbool.h>
#include <stdio.h>
bool zero_fuel(double distance_to_pump, double mpg, double fuel_left)
{
   return distance_to_pump <= mpg * fuel_left;
}

int main(){

double a= 60.000000,b = 30.000000, c =3.000000;

printf("%d\n",zero_fuel(a,b,c));

return 0;

}