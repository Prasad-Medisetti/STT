#include<stdio.h>
int main()
{
	int a[100],b[3]={0},i=0,j,n,size,c;
	printf("Enter size");
	scanf("%d",&size);
	printf("Enter numbers");
	while(i<size)
	{
		scanf("%d",&a[i]);
		c=a[i];
		b[c]++;
		i++;
	}
	for(i=0,j=0,n=0;n<size;)
	{
		if(j<b[i])
		{
			a[n]=i;
			n++;
			j++;
			
		}
		else
		{
			j=0;
			i++;
		}
	}
	for(i=0;i<size;i++)
	{
		printf("%d",a[i]);
		
	}return 0;
}
