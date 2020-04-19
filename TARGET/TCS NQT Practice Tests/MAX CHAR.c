//you as a developer,write a logic to find maximum valued character  from a given string without using default functions.
//For example:
//
//Test	Input 					Result
//1 		technical hub 		u
2 			python programming 	y

#include<stdio.h>
int maxChar(char *s) {
	int max = -1, i;
	for (i = 0; s[i] != '\0'; i++) {
		if (s[i] > max)
		   max = s[i];
	}
	return max;
}
int main() {
	char s[100],max;
	scanf("%[^\n]s",s);
	max = maxChar(s);
	printf("%c",max);
	return 0;
}
