#include <stdio.h>
int main()
{
	FILE *fp;
	char name[50],ch;
	int n=3,age,i;
	fp = fopen("1819\\f182019.txt","w+");
	if(fp == NULL)
	{
		printf("Could not open file.");
		return 1;
	}
	
	printf("Enter Name & Age seperated by a space:\n");
	for(i=0;i<n;i++)
	{
		printf("Enter Name & Age seperated by a space:\n");
		scanf("%s %d",&name, &age);
		printf(fp,"%d %s %d\n",i+1,name,age);
	}
	printf("Data Copied to file successfully");
	fclose(fp);
	return 0;
}
