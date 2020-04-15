#include<stdio.h>
int main()
{
	int n=10,i,temp,ele,pos;
	int a[10]={1,2,3,4,5,6,7,8,9,10};
//	printf("Enter the elements:");
//	for(i=0;i<10;i++)
//	 scanf("%d",&a[i]);
    printf("Enter the element to be inserted and position at?:");
    scanf("%d%d",&ele,&pos);
    n++;
       //temp=a[pos];
      for(i=n-1;i>pos-1;i--)
      {
      	a[i]=a[i-1];
	  }
	  a[pos-1]=ele;
    
	 printf("\nAfter inserting:");
		for(i=0;i<n;i++)
	 printf("%d ",a[i]);
	 return 0;
}
