#include<stdio.h> 
void reverse(char *a) 
{
	if(*a!='\0')
	reverse(a+1);
	printf("%c",a);
} 
int main() 
{ 
   char a[]="welcome"; 
   reverse(a); 
   return 0; 
} 


