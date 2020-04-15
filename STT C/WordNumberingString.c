#include <stdio.h>
int main()
{
	int i=0, j = 0,x=0;
	char str[100]={'\0'};
	printf("Enter a String: \n");
   	scanf("%s", &str);
   	for(i=0;str[i] != '\0';i++)
   	{
	    	if(str[i] != ' ')
		    {
	 			printf("%2d --> ",i+1);
	 			for(j=0;j != ' ';j++)
	 			{
			  		printf("%c",str[x++]);
				}
				printf(" %d",j);
			}
 			else
 			{
 				x++;
	 			printf("\n");
			}
	}
	return 0;
}
