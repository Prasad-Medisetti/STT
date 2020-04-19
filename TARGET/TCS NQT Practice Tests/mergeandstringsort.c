//Read Two Strings and we have to concatenate as 3rd string And we have to display the 3rd string in alphabetical order
//
//Sample Input:
//sudhir
//reddy
//Sample Output:
//dddehirrsuy
//
//For example:
//
//Test	Input	Result
//1		sudhir	dddehirrsuy
//		reddy	
//2		ravi	aaeijrtv
//		teja
//3 		siva	aaadiprssv
//		prasad
//4		phani 	aahikmnpru
//		kumar


//#include<stdio.h>
//int len(char *s) {
//	int i = 0;
//	for (i=0; s[i]!=0; i++);
//	return i;
//}
//int main() {
//	char s1[100], s2[100],s3[100],j,temp;
//	gets(s1);
//	gets(s2);
//	int i=0, ls1, ls2,ls3;
//	ls1 = len(s1);
//	ls2 = len(s2);
//	ls3 = ls1+ls2;
//	for (i=0;i<ls1+ls2;i++) {
//		if(i<ls1) 
//			s3[i]=s1[i];
//		if(i>=ls1)
//  		    s3[i]=s2[i-ls1];
//	}
//	for (i = 0; i < ls3-1; i++) {
//      for (j = i+1; j < ls3; j++) {
//         if (s3[i] > s3[j]) {
//            temp = s3[i];
//            s3[i] = s3[j];
//            s3[j] = temp;
//         }
//      }
//   }
//	printf("%s %s %s", s1, s2, s3);
//	return 0;
//}


#include <stdio.h>
#include <string.h>
int main()
{
    char a[100], b[100];
    scanf("%s",a); 
    scanf("%s",b); 
    strcat(a,b);
    int n = strlen(a),i,j;
    char temp;
    for (i = 0; i < n-1; i++) {
      for (j = i+1; j < n; j++) {
         if (a[i] > a[j]) {
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
         }
      }
       }
    printf("%s", a);
}
