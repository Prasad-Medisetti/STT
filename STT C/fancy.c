#include<stdio.h>
int main()
{
	int n,a,b,cnt1=0,cnt2=0;
	printf("Enter a 4 digit no:");
	scanf("%d",&n);
	while(n>0)
	{
		a=n%10;
		n=n/10;
		b=n%10;
		if(a==b)
		cnt1++;
		else if(a-1==b)
		cnt2++;
	}
	if(cnt1==2||cnt2==2)
	printf("Fancy number");
	else
	printf("not a fancy number");
	 return 0;
}
