#include<stdio.h>
int main(){
	int i,n=11,a[11]={-1,-36,-36,-2,0,-2,-36,-18,-12,-13,14},sum=0,max=0;
	for(i=0;i<n;i++)
	{
		sum+=a[i];
		
		if(sum>max)
		{
			max=sum;
		}
		if(sum<0)
		{
			sum=0;
		}
		
	}
	printf("%d",max);
}
