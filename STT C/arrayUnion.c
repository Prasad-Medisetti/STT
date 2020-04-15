#include<stdio.h>
int main()
{
	int n1,n2,i,j,k,flag=0,l;
	printf("Enter the sizes of sets: ");
	scanf("%d%d",&n1,&n2);
	int a[n1],b[n2];
	printf("Enter the elements of set1:");
	for(i=0;i<n1;i++)
	  scanf("%d",&a[i]);
  	printf("Enter the elements of set2:");
	for(i=0;i<n2;i++)
	  scanf("%d",&b[i]);
    //union
    int n3=n1+n2;
	int c[n3];
	l=n3-n1;
    for(i=0;i<n1;i++)
    	 c[i]=a[i];
  	 for(i=0;i<n1;i++)
  	 {
  	  for(j=0;j<n2;j++)
  	    if(a[i]==b[j])
  	    {
  	     flag=1;
  	     break;
  	    }
  	    if(flag==0)
  	    {
  	    c[l]=b[j];
  	    l++;
  	    }
	}
   
   	for(i=0;i<n3;i++)
	  printf("%d ",c[i]);
}
