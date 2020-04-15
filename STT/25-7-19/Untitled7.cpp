#include<stdio.h>
#include<string.h>
char* reverse(char *s,int i,int j);
int main()
{
   char a[100];
   int n;
   printf("Enter a string\n");
   gets(a);
   n=strlen(a);
   reverse(a,0,n-1);
   printf("Reversed string\n%s",a);
   return 0;
}
char* reverse(char *s,int i,int j)
{
      char ch;
      if(NULL==s||i>j)
        return NULL;
      ch=s[i];
      s[i]=s[j];
      s[j]=ch;
      reverse(s,i+1,j-1);
      return s;
}
