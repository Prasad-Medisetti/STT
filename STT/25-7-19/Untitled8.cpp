#include<stdio.h> 
int reverse(char *str) 
{ 
   if (*str!='\0') 
   {
    	reverse(str+1); 
    	printf("%c",*str);
   }  
    return 0;
} 
int main() 
{ 
   char a[]="welcome"; 
   reverse(a); 
   return 0; 
} 


