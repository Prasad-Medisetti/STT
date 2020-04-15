#include <stdio.h>
int main()
{
	int ch;
	FILE *fp;
//	Reading files
	fp = fopen("STT.txt","r");
	if(fp == NULL)
	{
		printf("ERROR OCCURED WHILE OPENING FILE\n");
		exit(1);
	}
	while((ch=fgetc(fp)) != EOF)
	{
		printf("%c",ch);
	}
	fclose(fp);
	return 0;
}
