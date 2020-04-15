#include<stdio.h>
int main()
{
	char a[100],c;
	int i=0;
	while(1)
	{
		scanf("%c",&c);
		if(c=='1')
		break;
		a[i++]=c;
	}
	//a[i]='\0';
	printf(a);
	return 0;
}

