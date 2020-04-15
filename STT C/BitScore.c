#include<stdio.h>
#include<stdlib.h>
int countDigit(int n) 
{ 
    int count = 0; 
    while (n != 0) 
	{ 
        n = n / 10; 
        ++count; 
    } 
    return count; 
} 
int main()
{
	int n , i, j=0, max, min, score, r, k=0, t;
	printf("Enter no.of elements:\n");
	scanf("%d",&n);
	int a[n],s[n];
	printf("Enter elements:\n");
	for(i=0;i<n;i++)	
		scanf("%d",&a[i]);
	for(i=0;i<n;i++)
	{
		score=0;
		r=a[i]%10;
		min=max=r;
		while(a[i]>0)
		{
		 r=a[i]%10;
	     a[i]=a[i]/10;
	     if(max<r)
	       max=r;
         if(min>r)
           min=r;
         score=min*7+max*11;
         }
         if(countDigit(score)>=3)
         {
         	while(j<2)
         	{
         		t=score%10;
         		score=score/10;
         		k=t*pow(10,j)+k;
         		j++;
			 }
			 s[i]=k;
		 }
		 else
          s[i]=score;
	}
	for(i=0;i<n;i++)
	  printf("%d ",s[i]);
	return 0;
}
/*
	Test output
	299 512 123
	13 62 40
*/
