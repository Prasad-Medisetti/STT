#include <stdio.h>
int main()
{
	char para[100], count[25] = {0}, count1[25] = {0};
	int i,j,k;
	printf("Enter a paragraph with spaces, new lines: \n");
	scanf("%[A-za-z \n]",para);
	for(i = 0;para[i] != '\0';i++)
//		printf("%c",para[i]);
	{
		for(j=97,k=65;j<=122 || k<=90;j++,k++)
		{
			if(para[i] == j)
				count[j-97]++;
			if(para[i] == k)
				count1[k-65]++;
		}
	}
	system("cls");
	printf("Entered paragraph is:\n%s\n\n",para);
	for(i=97,j=65;i<=122 || j<=90;i++,j++)
		printf("\t%c : %3d times.\t\t%c : %3d times.\n",i,count[i-97],j,count1[j-65]);
	return 0;
}
