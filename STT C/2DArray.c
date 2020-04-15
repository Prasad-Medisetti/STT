#include <stdio.h>
int main()
{	int i, j;
	char a[5][100];
//	char a[][10] = {"aditya", "sri", "sai"};

//	for(i = 0;i < 3;i++)
//	{
//		for(j = 0;j < 2;j++) 
//			printf("%d \t",a[i][j]);
//		printf("\n", a[i]);
//	}
	int x, y;
	for(i = 0;i < 5;i++)
		gets(a[i]);
	printf("Enter 2 positions: \t");
	scanf("%d%d", &x, &y);
//	scanf("%[a-zA-z \n]", a);
	for(i = 0;i < 5;i++)
	{
		for(j = x;j <= y;j++)
			printf("%c", a[i][j]);
		printf("\n");
	}
	return 0;
}
