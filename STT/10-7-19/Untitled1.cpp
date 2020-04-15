#include<stdio.h>
int main()
{
	int i,a[20]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20},start,end,count,sum;
	printf("Enter start,end and stepcount values");
	scanf("%d%d%d",&start,&end,&count);
	for(i=start;i<end;i=i+count)
	printf("%d ",a[i]);
	return 0;
	
}
