#include<stdio.h>
int main()
{
	char a[7]="ADITYA";
	int i,j,k,l,n;
	printf("Enter n value");
	scanf("%d",&n);
	for(i=1;i<=2*n-1;i++)
	{
		k=i<=n?i:n-(i%n);
		
		for(j=1;j<=k;j++)
		{
			printf("%c",a[i]);
		}
		printf("\n");
	}
	return 0;
}

	
