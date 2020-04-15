#include<stdio.h>
#include<math.h>
int main()
{
	float n,a,b;
	printf("Enter a number: ");
	scanf("%f",&n);
	a=floor(sqrt(n));
	if(a*a==n)
	printf("\n%g",a*a);
	else{
	
	b=a+1;
	if((n-a*a)<(b*b-n))
	 printf("Nearest square is: %g",a*a);
    else
  	printf("Nearest square is: %g",b*b);
  }
  	return 0;
	   
}
