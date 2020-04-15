#include<stdio.h>
#include<string.h>
int main()
{
	char a[100],b[100],c[100];
	int i,j,n,k=0;
	printf("\nEnter string size:");
	scanf("%d",&n);
	printf("\nEnter string:");
	for(i=0;i<n;i++)
		scanf("%s",a[i]);
	
		for(i=0;i<n;i++)
		{
			if(a[i]!=32)
			{
				b[k]=a[i];
				k++;
			}
			else
			{
				for(k=i,j=0;k>0;k--,j++)
				{
					c[j]=b[k];
				}
			}
		}
		for(j=0;j<n;j++)
		{
			printf("%c",c[j]);
		}
	return 0;
}
