//Write A Program to find second most frequent character in a given string and display messages as shown below.
//
//Examples:
//Input: aabababa
//Output: Second most frequent character is : b
//
//Input: GeeksforGeeks
//Output: Second most frequent character is : G
//
//Input: abcd
//Output: No Second most frequent character
//
//For example:
//
//Test 	Input			Result
//1 	aabababa 		Second most frequent character is : b
//2		GeeksforGeeks 	Second most frequent character is : G
//3		abcd			No Second most frequent character

//#include <stdio.h>
//char secondmostfreq(char *s){
//    int count[256]={},i;
//    char first='(',second='(';
//    for(i=0;s[i]!='\0';i++){
//        count[(int)s[i]]++;
//    }
//    for (i = 0; s[i]!='\0'; i++) {
//    	if(first==s[i])
//    		continue;
//        if(count[(int)s[i]]>count[(int)first]){
//            second=first;
//            first=s[i];
//        }
//        else{
//        	if(count[(int)s[i]]>count[(int)second]){
//        		second=s[i];
//			}
//		}
//    }
//    if(count[(int)first]==count[(int)second]){
//    	return 0;
//	}
//    return second;
//}
//int main() {
//    char inp[100],temp;
//    scanf("%s",inp);
//    temp=secondmostfreq(inp);
//    if(temp){
//    	printf("Second most frequent character is : %c",temp);
//	}
//    else{
//    	printf("No Second most frequent character");
//	}
//    return 0;
//}


#include <stdio.h>
char secondmostfreq(char *s){
    int count[256]={},i;
    char first='(',second='(';
    for(i=0;s[i]!='\0';i++){
        count[(int)s[i]]++;
    }
    for (i = 0; s[i]!='\0'; i++) {
    	if(first==s[i])
    		continue;
        if(count[(int)s[i]]>count[(int)first]){
            second=first;
            first=s[i];
        }
        else{
        	if(count[(int)s[i]]>count[(int)second]){
        		second=s[i];
			}
		}
    }
    if(count[(int)first]==count[(int)second]){
    	return 0;
	}
    return second;
}
int main() {
    char inp[100],temp;
    scanf("%s",inp);
    temp=secondmostfreq(inp);
    if(temp){
    	printf("Second most frequent character is : %c",temp);
	}
    else{
    	printf("No Second most frequent character");
	}
    return 0;
}
