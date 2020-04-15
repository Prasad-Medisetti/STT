#include <stdio.h>
int main()
{
	int i=0, flag = 0;
	char str1[20], str2[20];
	printf("Enter 1st String: \n");
   	scanf("%s", &str1);
	printf("Enter 2nd String: \n");
   	scanf("%s", &str2);
   	for(i = 0;str1[i] != '\0';i++)
   		if(str1[i] != str2[i])
   		{
   		  	printf("Not Equal");
   		  	return;   		  	
		}
	printf("Equal");
//	for(i=0;i<20;i++)
//	{
//		if(str1[i] == str2[i])
//		{
//  			flag = 1;
//  			break;
//		}
//	}
//	if (flag == 1)
//	   	printf("EQUAL");
// 	else
//	 	printf("NOT EQUAL");
	return 0;
}
