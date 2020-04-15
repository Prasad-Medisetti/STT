#include<stdio.h>
int main()
{
	int a;
	printf("Enter a number: 1 or 2\n");
	scanf("%d",&a);
	switch(a)
	{
		case 1:
			if(a==1)
			break;
		case 2:
			while(a == 2)
			{
				if(a == 2)
				a--; 
				continue;
			}
			break;
		default:
			printf("INVALID");
	}
}
