#include<stdio.h>
int main()
{
	int b[26]={0},i,n;
	char a[100],e='a',c,d;
	printf("Enter string size:");
	scanf("%d",&n);
	printf("Enter string:");
	for(i=0;i<=n;i++)
	{
		scanf("%c",&a[i]);
	}
	for(i=0;i<=n;i++)
	{
		c=a[i];
		if(c>=65&&c<=90)
		{
			c=c+32;
		}
		if(c>=97&&c<=122)
		{
			d=c-97;
			(b[d])++;
		}
	}
	for(i=0;i<26;i++)
	{
		if(b[i]!=0)
		{
			printf("%c %d\n",(e+i),b[i]);
		}	
	}
	return 0;
}
