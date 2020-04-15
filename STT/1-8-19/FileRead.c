#include <stdio.h>
int main()
{
	FILE *fp;
	char data[50],ch;
	fp = fopen("FileRead.c","r");
	if(fp == NULL)
	{
		printf("Could not open file.");
		return 1;
	}
	printf("File Contains the following :\n");
	while((ch=fgetc(fp))!=EOF)
	{
		printf("%c",ch);
	}
	printf("EOF");
	fclose(fp);
	return 0;
}
