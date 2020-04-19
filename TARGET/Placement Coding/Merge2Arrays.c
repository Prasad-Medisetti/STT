#include<stdio.h>
int merge(int a1[], int l1, int a2[], int l2) {
	int l = l1+l2;
	int i, j, a3[100];
	for (i=0;i<l1;i++)
	{
		printf("%d ",a1[i]);
	}
	printf("\n");
	for (i=0;i<l2;i++)
	{
		printf("%d ",a2[i]);
	}
	for(i=0; i<l1;i++)
 	{
 		a3[i]=a1[i];
	}
	printf("%d\n",i);
	for(i=l1, j = 0;i<20 && j<=l2;i++,i++)
	{
		a3[i]=a2[j];
	}
	for (i=0;i<100;i++)
	{
		printf("%d ",a3[i]);
	}
	return 1;
}
void main() {
	int a, a1[10] = {1, 2, 3, 4}, a2[10] = {5, 6, 7, 8}, a3[20], i;
	int l1 = 4, l2=4;
//	for (i=0;i<l1;i++)
//	{
//		printf("%d ",a1[i]);
//	}
//	printf("\n");
//	for (i=0;i<l2;i++)
//	{
//		printf("%d ",a2[i]);
//	}
	
	printf("\n");
	a = merge(a1,4,a2,4);
//	for (i=0; i<)
}
