#include<stdio.h>
int LCM(int a, int b)
{
	int i=1;
	if(a<b)
	 i=a;
	 else
	  i=b;
	for(;i<=a*b/2;i++)
	 {
	 	if(i%a==0&&i%b==0)
	 	{
	 	 printf("LCM is %d",i);
	 	 break;
	    }
	 }
}
void main()
{
	int i,a,b;
	printf("Enter two numbers: ");
    scanf("%d%d",&a,&b);
	LCM(a,b);
}
