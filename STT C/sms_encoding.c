/*
1.	Write a C function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence 
	to be sent as SMS and returns the abbreviated sentence. 
	Rules are as follows: 
	a. Spaces are to be retained as is 
	b. Each word should be encoded separately
	If a word has only vowels then retain the word as is
	If a word has a consonant (at least 1) then retain only those consonants
	Note: Assume that the sentence would begin with a word and there will be only a single space between the words. 

	Sample Input									Expected Output
	I love Python									I lv Pythn
	MSD says I love cricket and tennis too			MSD sys I lv crckt nd tnns t
	I will not repeat mistakes						I wll nt rpt mstks
*/
#include <stdio.h>
void sms_encoding();
int check_vowel(char);
char str[100];
int main()
{
	printf("Enter a Sentence:\n");
	gets(str);
	sms_encoding();
	printf("Encoded Message:\t\"%s\"",str);
	return 0;
}
int check_vowel(char s)
{
	if(s=='a'||s=='e'||s=='o'||s=='i'||s=='u')
		return 1;
	else
		return 0;
}
void sms_encoding()
{
//	int i,j;
//	for(i=0;str[i]!='\0';i++)
//	{
//		if(check_vowel(str[i]) == 1)
//		{
//			for(j=i;str[j]!='\0';j++)
//				str[j] = str[j+1];
//			i=0;
//		}
//	}
	char *p,*q;
	for(p=str;*p!='\0';p++)
	{
		if(check_vowel(*p) == 1)
		{
			for(q=p;*q!='\0';q++)
				*q=*(q+1);
			p=str;
		}
	}
	return;
}
