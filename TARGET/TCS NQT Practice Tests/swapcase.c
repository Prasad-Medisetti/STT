//Write A Program to Convert every word first char to upper case and other char to lowercase of a given string and display output as shown below.
//
//Input: My name is Suresh
//
//Output :  mY nAME iS sURESH
//
//input: i am expert in java
//
//output : i aM eXPERT iN jAVA
//
//input: FAMILIAR WITH RPA
//output: fAMILIAR wITH rPA
//
//For example:
//
//Test	Input				Result
//1 	My name is Suresh 	mY nAME iS sURESH
//2 	i am expert in java i aM eXPERT iN jAVA
//3		FAMILIAR WITH RPA	fAMILIAR wITH rPA

#include<stdio.h>
#include<string.h>
char *  fun(char *s) {
	int i=0;
	if(s[i]>='A' && s[i]<='Z') {
		s[i]+=32;
	}
    i+=1;
    while(s[i]!='\0') { 
		if (s[i-1]==' ') {
 		    if(s[i]>='A' && s[i]<='Z') {  
	            s[i]+=32;
			}
		}      
        else if(s[i]>='a' && s[i]<='z') {
          s[i] -= 32;  
        }
        i++;
     }
	return s;
}
int main() {
	char s[100], *res;
	scanf("%[^\n]s",s);
	res = fun(s);
	printf("%s",res);
	return 0;
}
