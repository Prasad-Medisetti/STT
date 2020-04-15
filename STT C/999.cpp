#include<stdio.h>
#include<math.h>
int main()
{
	int n = 2;
	for(i=1;i<=n;i++)
	{
		k=i<=n?i:n-(n%i);
		for(j=0;j<k;j++)
		 printf(" ";);
	}
 
}
