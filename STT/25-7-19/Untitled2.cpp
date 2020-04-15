#include<stdio.h>
void add(int [],int);
int main()
{
	int a[10]={0};
	int i;
	for(i=0;i<10;i++)
	printf("%d\n",a[i]);
	add(a,10);
	for(i=0;i<10;i++)
	printf("%d\n",a[i]);
	return 0;
}
void add(int a[],int n)
{
	int i;
	for(i=0;i<10;i++)
	a[i]++;
	return;
}
