#include <stdio.h>
#include <string.h>
int main()
{
    char name[5][10],item[10]="\n";
	int i,x,count=0;
    printf("Enter 5 strings:\n");
    for(i=0 ;i<5 ;i++ )
        scanf("%s",&name[i][0]);
    for(i=0; i<5 ;i++ )
	{
        x=strcmp(&name[i][0],item);
        if(x == 1)
        count++;
    }
	return 0;
}
