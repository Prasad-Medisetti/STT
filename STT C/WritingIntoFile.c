#include <stdio.h>
int main()
{
	int ch;
	FILE *fp;
//	Writing into files
	fp = fopen("STT.txt","w+");
	if(fp == NULL)
	{
		printf("ERROR OCCURED WHILE OPENING FILE\n");
		exit(1);
	}
	while((ch=getchar()) != '~')
	{
		fputc(ch,fp);
	}
	fclose(fp);
	return 0;
}
