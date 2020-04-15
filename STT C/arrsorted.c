#include<stdio.h>
int main()
{
  int n=5,i,cnt1=0,cnt2=0;
   int a[n];
     for(i=0;i<n;i++)
       scanf("%d",&a[i]);
      for(i=0;i<n-1;i++)
       {
          if(a[i]<a[i+1])
             cnt1++;
           if(a[i]>a[i+1])
             cnt2++;
       }
      if(cnt1==0 || cnt2==0)
         printf("Sorted");
       else
         printf("not sorted");
}

