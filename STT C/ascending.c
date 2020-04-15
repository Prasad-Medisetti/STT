#include<stdio.h>
void main()
{
 int n,a,b,cnt=0,d;
 printf("Enter a number: ");
 scanf("%d",&n);
 d=printf("%d",n);
 while(n>0)
 {
 	a=n%10;
 	n=n/10;
 	b=n%10;
 	if(a>b)
     cnt++;
 }
 if(cnt==d)
   printf(" is in ascending order!");
 else
   printf(" is not in an ascending order!");
   
}
