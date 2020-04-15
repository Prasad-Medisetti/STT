#include<stdio.h>
int main()
{
	int n=10,i,flag=0,ele,pos;
	int a[10]={1,2,3,4,5,6,7,8,9,10};
//	printf("Enter the elements:");
//	for(i=0;i<10;i++)
//	 scanf("%d",&a[i]);
    printf("Enter the element to be deleted: ");
    scanf("%d",&ele);
     for(i=0;i<n;i++)
     {
     	if(a[i]==ele)
     	{
     	  pos=i;
     	  break;
        }
   	   else 
   	     flag++;
	 }
    n--;
      for(i=pos;i<n;i++)
      {
      	a[i]=a[i+1];
	  }
     if(flag==10)
       printf("Element not found");
     else{
	 printf("\nAfter deleting:");
		for(i=0;i<n;i++)
	 printf("%d ",a[i]);
}
	 return 0;
}
