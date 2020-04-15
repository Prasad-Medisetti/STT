#include <stdio.h>
int main()
{
	int i=0, cnt = 0;
	char ch;
	printf("Enter a character: \n");
   	scanf("%c", &ch);
   	if(ch>=48 && ch<=57)
 		printf("%c is a Digit.",ch);
	else if((ch>=65 && ch<=90) || (ch>=90 && ch<=122))
 		printf("%c is a Alphabet.",ch);
	else
 		printf("%c is a Special Character.",ch);
	return 0;
}
