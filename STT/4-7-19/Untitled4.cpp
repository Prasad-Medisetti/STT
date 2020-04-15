#include<stdio.h>
int main()
	{
       int num;
       char flag = false;
       printf("Enter number");
       scanf("%d",&num);
       int present = num % 10;
       num = num/10;
       while(num>0)
	   {
           if(present <= num % 10){
               flag = true;
               break;
           }

           present = num % 10;
           num = num/10;
       }
       if(flag)
	   {
           printf("Digits are not in increasing order.");
       }else
	   {
           printf("Digits are in increasing order.");
       }return 0;
    }

