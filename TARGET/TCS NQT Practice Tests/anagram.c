//Write A Program to Check whether two given Strings are Anagrams and display output as shown below.
//Two strings are called anagrams if they contain same set of characters but in different order.
//
//For example:
//Test	Input			Result
//1		keep			keep and peek are anagrams
//		peek
//2		Mother In Law	MotherInLaw and HitlerWoman are anagrams
//		Hitler Woman	
//3		suresh			suresh and java are not anagrams
//		java


#include <stdio.h>
#include<ctype.h>
#include <string.h>
int anag(char *s1,char *s2)
{
   int i, j,n,n1;
   char temp,a[20],b[20];
   strcpy(a,s1);
   strcpy(b,s2);
   n  = strlen(s1);
   n1 = strlen(s2);
   if( n != n1)
    {    
      return 0;
   }
    for (i = 0; i < n-1; i++) 
	{
      for (j = i+1; j < n; j++) 
	  {
         if (s1[i] > s1[j])
		  {
            temp  = s1[i];
            s1[i] = s1[j];
            s1[j] = temp;
         }
         if (s2[i] > s2[j])
		  {
            temp  = s2[i];
            s2[i] = s2[j];
            s2[j] = temp;
         }
      }
   }
   
   for(i = 0; i<n; i++) 
   {
      if(s1[i] != s2[i]) {    
         return 0;
      }
   }
   return 1;
}
int main () 
{
   char s1[20],s2[20],a[20],b[20];
   int i,j=0,res;
   scanf("%[^\n]s\n",s1);
   scanf(" %[^\n]s\n",s2);
   for(i=0;s1[i]!='\0';i++)
   {
   	if(s1[i]==' ')
   		continue;
 	s1[j]=s1[i];	
    a[j]=tolower(s1[i]);
    j++;
   }
   s1[j]=a[j]='\0';
   j=0;
   for(i=0;s2[i]!='\0';i++)
   {
   	if(s2[i]==' ')
   		continue;
  		s2[j]=s2[i];
    b[j]=tolower(s2[i]);
    j++;
   }
   s2[j]=b[j]='\0';
   res=anag(a,b);
   if(res==0)
   	  printf("%s and %s are not anagrams",s1,s2);
  	else
  	  printf("%s and %s are anagrams",s1,s2);
}
