#include <stdio.h>
int main()
{
	int s,i,start,end,step;
	printf("Enter no.of Elements: \t");
	scanf("%d",&s);
	int a[s];
	printf("Enter the Elements: \n");
	for(i=0;i<s;i++)
		scanf("%d",&a[i]);			
	printf("Enter start, end indices and step count: \t");
	scanf("%d%d%d",&start,&end,&step);
	printf("Entered Elements in range(%d,%d) are: \n",start,end);
	for(i=start-1;i<end;i += step)
		printf("%d ",a[i]);
	return 0;
}
