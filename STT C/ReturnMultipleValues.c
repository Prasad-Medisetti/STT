#include <stdio.h>
int* display(int [],int,int*);
int main()
{
	int a[]={1,2,3,4,5,6,7,8},*b,res_count,i,n=8;
	b = display(a,n,&res_count);
	for(i=0;i<res_count;i++)
		printf("%d ",*(b+i));
	return 0;
}
int* display(int x[],int n,int* c)
{
	int i,k=0;
	static int p[8];
	for(i=0;i<n;i++)
		if(x[i]%2==0)
			p[k++] = x[i];
	*c = k;
	return p;
}
