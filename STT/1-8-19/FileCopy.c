#include<stdio.h>
int main()
{
	FILE *fp1,*fp2;
	int ch;
	fp1 = fopen("hello.txt","r");
	fp2 = fopen("helloworld.txt","w+");
	if(fp1==NULL)
	{
		printf("Error in File Opening.");
		exit(1);
	}
	while((ch=fgetc(fp1)) != EOF)
	{
		fputc(ch,fp2);
	}
	printf("File Copied Successfully.");
	return 0;
}
