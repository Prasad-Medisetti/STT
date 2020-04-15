#include <stdio.h>
int main()
{
	char ch;
//	while((ch = getchar()) != '1') // getchar() is line buffered.
//		putchar(ch);
//	while((ch = getche()) != '1') // getche() is not line buffered.
//		putchar(ch);
	while((ch = getch()) != '1') // getch() is not line buffered.
		putchar(ch);
	return 0;
}
