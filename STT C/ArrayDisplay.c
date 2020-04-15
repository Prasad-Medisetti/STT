#include <stdio.h>
void display();
int main()
{
	display();
	display();
	display();
//	printf("%d\n",x);
	return 0;
}
void display()
{
	static int x = 1;
	printf("%d\n",x);
	x++;
	return;
}
