 #include<stdio.h>
 int main()
 {
 	int n,i,start,step,end;
 	printf("Enter size:");
 	scanf("%d",&n);
	 int a[n];
	 printf("Enter the elements:");
	 for(i=0;i<n;i++)
	    scanf("%d",&a[i]);
     printf("Enter starting,ending indices and step count: ");
     scanf("%d%d%d",&start,&end,&step);
      for(i=start-1;i<end-1;i+=step)
        printf("%d ",a[i]);
	  return 0;
 }
