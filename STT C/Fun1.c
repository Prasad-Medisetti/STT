#include <stdio.h>
//void add(int*,int);
//int main()
//{
//	int a=23,b=23;
//	add(&a,b);
//	printf("%d, %d",a,b);
//	return 0;
//}
//void add(int *a,int b)
//{
//	*a=*a+1;
//	b=b+1; 
//	return;
//}
void add(int [],int);
int main()
{
	int a[10]={0};
	add(a,10);
	return 0;
}
void add(int a[],int n)
{
	int i;
	for(i=0;i<n;i++)	
		printf("%d\n",a[i]);
	return;
}
