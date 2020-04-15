#include<stdio.h>
int main()
{
	int a[10]={0},i,n;
	printf("Enter your elements: (0-9) (-1 to stop)\n");
	do{
		scanf("%d",&n);
		switch(n)
		{
			case 0:	a[0]++;break;
			case 1:	a[1]++;break;
			case 2:	a[2]++;break;
			case 3:	a[3]++;break;
			case 4:	a[4]++;break;
			case 5:	a[5]++;break;
			case 6:	a[6]++;break;
			case 7:	a[7]++;break;
			case 8:	a[8]++;break;
			case 9:	a[9]++;break;
			default: break;	
		}
	}while(n!=-1);
	for(i=0;i<10;i++)
	 printf("\n%d is repeated %2d times.",i,a[i]);
}
