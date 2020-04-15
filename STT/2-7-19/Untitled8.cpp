#include<stdio.h>
int main()
{
	int tally=0;
	for(; ;)
	{
	if(tally==10)
	break;
	printf("%d",++tally);
}
return 0;
}
