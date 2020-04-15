#include<stdio.h>
int main()
{
	char a[100],b[26],c[100];
	int i,j=0,n,k=0;
	printf("\nEnter new string order:");
	for(i=0;i<26;i++)
	{
		scanf("%c",&b[i]);
	}
	printf("\nEnter string size:");
	scanf("%d",&n);
	printf("\nEnter string:");
	for(i=0;i<n;i++)
	{
		scanf("%c",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<26;j++)
	{
		if(a[i]==b[j])
		{
			printf("%c",a[i]);
		}
	}
	
	}
	return 0;
}
