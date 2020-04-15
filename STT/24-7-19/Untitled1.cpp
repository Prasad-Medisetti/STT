#include<stdio.h>
#include<string.h> 
int main()
{
	char str[]="abcd";
	int n,len,i,j,k;
	n=strlen(str); 
    for ( len = 1; len <= n; len++)  
    {     
        for ( i = 0; i <= n - len; i++)  
        { 
            j = i + len;             
            for ( k = i; k<j; k++)
			{
                printf("%c",str[k]); 
        	} 
        printf("\n");
    	} 
	}
} 
