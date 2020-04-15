#include <stdio.h>
int main()
{
	int i=0, cnt = 0;
	char str[20];
	printf("Enter a String: \n");
   	scanf("%s", &str);
   	for(i=0;str[i] != '\0';i++)
   		if(str[i]>='0' && str[i] <= '9')
   		    continue;
		else
		{
			printf("No");
			return 0;   
		}		
	printf("Yes");
	return 0;
}
