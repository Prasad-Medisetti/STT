#include <stdio.h>
int main()
{
	int i=0, cnt = 0;
	char str1[20];
	printf("Enter String: \n");
   	scanf("%s", &str1);
   	for(i = 0;str1[i] != '\0';i++)
   		if(str1[i] < str1[i+1])
   		{  	
   			cnt++;
		}
	if(cnt == i-1)
   		printf("In Strictly Alphabetical Order.");
	else
		printf("Not In Strictly Alphabetical Order.");
	return 0;
}
