//Palindrome.c
#include<stdio.h>

//CODE 1
//void main() {
//	int num, r, rev, num1;
//	scanf("%d", &num);	// 123
//	num1 = num;
//	while (num != 0) {	// 123 != 0, 12 != 0, 1 != 0
//		// 123	123%10==3
//		r = num % 10;	// r = 3, 2, 1 ---> 321
//		num = num / 10;	// num = 12, 1, 0
//		rev = rev * 10 + r;	// 3, 32, 321
////		printf("%d %d", num, rev);
//	}
//	if (num1 == rev)
//	   printf("Palindrome");
//	else 
//	   printf("Not Palindrome");
//}

// CODE 2 WITH FUN
int reverse(num) {	// fun def
	int r, rev = 0;
	while (num != 0) {	// 123 != 0, 12 != 0, 1 != 0
		// 123	123%10==3
		r = num % 10;	// r = 3, 2, 1 ---> 321
		num = num / 10;	// num = 12, 1, 0
		rev = rev * 10 + r;	// 3, 32, 321
	}
	return rev;
}

void main() {
	int num, rev;
	scanf("%d", &num);	// 123
	rev = reverse(num);
	if (num == rev)
	   printf("Palindrome");
	else 
	   printf("Not Palindrome");
}
