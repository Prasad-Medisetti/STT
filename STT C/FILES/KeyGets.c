#include <stdio.h>
int main()
{
	FILE *fp;
	char data[50];
	fp = fopen("1819\\f182019.txt","w");
	if(fp == NULL)
	{
		printf("Could not open file.");
		return 1;
	}
	printf("Enter some text from Keyboard\n");
	while(strlen(gets(data)) > 0)
	{
		fputs(data,fp);
		fputs("\n",fp);
	}
	printf("Closed the file.");
	fclose(fp);
	return 0;
}
