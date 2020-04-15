#include <stdio.h>
#include <math.h>
int main() 
{
    float  n,a,b;
    printf("Enter a number : \n");
    scanf("%f",&n);
//    printf ("%2.f %2.f\n",sqrt(n),round(sqrt(n)));
    a = round(sqrt(n));
    b = a+1;
    if((a*a-n > 0) <= (b*b-n > 0))
        printf("Nearest Square of %2.f is %2.f",n,a*a);
//    else 
//        printf("Nearest Square of %2f is %2f",n,b*b);
    return 0;
}