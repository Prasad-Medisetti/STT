#include<stdio.h>
void main()
{
    int n=5,i,j,u;
    int a[5],b[n];
    for(i=0;i<n;i++)
    scanf("%d",&a[i]);
    u=0;
    while(u<3)
    {
        for(i=0;i<n;i++)
        {
            if(a[i]==u)
             b[j++]=u;
        }
        u++;
    }
    for(i=0;i<n;i++)
     printf("%d ",b[i]);
}
