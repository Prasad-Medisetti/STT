#include<stdio.h>
int main()
{
	char a[100];
	//    char a[10]="aditya",i;
//char a[10]={'a','d','\0'};
//    for(i=0;i<10;i++)
//	  for(i=0;a[i]!='\0';i++)	
//      printf("%c\n",a[i]);
	//	printf(a);
      
//	char a[100],c;int i=0;
//	scanf("%s",a);
//   scanf("[^%s]",a);
//     gets(a);
//	while((c=getchar())!='1')
//	while(1)
//	{
//		 scanf(" %c",&c);
//		 if(c=='1')
//		  break;
//	    a[i++]=c;
//    }
//	a[i]='\0';
//	scanf("%[a-z \n]",a);
	scanf("%[^0-9]",a);
	printf(a);
}
