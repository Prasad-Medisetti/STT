#include <stdio.h>
int main()
{
	int m,n,s1,s2,i,ch;
	printf("Enter no.of Elements 1st and 2nd sets: ");
	scanf("%d%d",&s1,&s2);
	int a[s1],b[s2],c[s1+s2];
	printf("Enter 1st set Elements: \n");
	for(i=0;i<s1;i++)
		scanf("%d",&a[i]);	
	printf("Enter 2nd set Elements: \n");
	for(i=0;i<s2;i++)
		scanf("%d",&b[i]);		
	do
	{
		printf("\n1.Union\n2.Intersection\n3.Subtraction\n4.Exit");
		printf("\nEnter ur choice: ");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:
				for(i = 0;i<s1+s2;i++)
				{
					if(a[i] == b[i-s1])
						continue;
					else
						if(i<s1)
							c[i] = a[i];
						else
							c[i] = b[i-s1];
				}
				for(i=0;i<s1+s2;i++)
					printf("%d ",c[i]);
				break;
			case 2:
				break;
			case 3:
				break;
		}
	}while(ch != 4);
	return 0;
}
