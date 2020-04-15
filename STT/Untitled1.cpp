#include<stdio.h>
void reverse(int *,int,int);
int main()
{
	int a[10],i=0,n;
	printf("Enter array size");
	scanf("%d",&n);
	printf("\nEnter array elements");
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	reverse(a,i,n);
	return 0;
}
void reverse(int *a,int i,int n)
{
	if(i!=n)
	{
		i++;
		reverse(a+1,i,n);
		
	}	printf("%d ",*a);
	return ;
}

