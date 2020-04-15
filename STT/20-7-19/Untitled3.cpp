#include<stdio.h>
int main()
{
	char a[100],n,i;
	printf("Enter size:");
	scanf("%d",&n);
	printf("Enter string:");
	for(i=0;i<=n;i++)
	scanf("%c",&a[i]);
	for(i=0;i<=n;i++)
	{
		if((a[i]>=97&&a[i]<=122)||(a[i]>=65&&a[i]<=90))
		printf("%c",a[i]);
	}return 0;
}
