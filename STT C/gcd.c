#include<stdio.h>
int GCD(int a, int b)
{
	int i,n,c;
	if(a<b)
	n=a;
	else
	n=b;

	for(i=1;i<=n;i++)
	 {
	 	if(a%i==0&&b%i==0)
	 	{
	 	 c=i;
	    }
	 }
	 if(c==1)
	  printf("GCD is 1");
	  else
       printf("GCD is %d",c);
}
void main()
{
	int i,a,b;
	printf("Enter two numbers: ");
    scanf("%d%d",&a,&b);
	GCD(a,b);
}
