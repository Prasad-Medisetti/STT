#include<stdio.h>
int main()
{
   int n,a[15],i,k=0;
   scanf("%d",&n);
   for(i=1;i<=n;i++)
   { scanf("%d",&a[i]);}
   for(i=1;i<=n;i++)
   {
      if(a[i]<a[i+1])
         k++;
   }
   if(k==0)
      printf("yes");
   else
       printf("no");
	return 0;
}
