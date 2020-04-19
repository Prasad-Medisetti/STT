// 2nd large.c
#include<stdio.h>
//CODE 1
void main() {
	int size, num[100], i, max ,sm;
	scanf("%d", &size);	
	for (i = 0; i < size; i++)
		scanf("%d ", &num[i]);
	
	max = num[0];
	for (i=1; i< size; i++) {
		if (max<num[i])
		   max = num[i];
	}
	
	sm = num[0];
	for (i=1; i< size; i++) {
		if (sm<num[i] && max>num[i])
		   sm = num[i];
	}
	printf("%d %d\n", max,sm);
	for (i = 0; i < size; i++)
		printf("%d ", num[i]);
}


//int reverse(num) {	// fun def
//	int r, rev = 0;
//	while (num != 0) {	// 123 != 0, 12 != 0, 1 != 0
//		// 123	123%10==3
//		r = num % 10;	// r = 3, 2, 1 ---> 321
//		num = num / 10;	// num = 12, 1, 0
//		rev = rev * 10 + r;	// 3, 32, 321
//	}
//	return rev;
//}
//
//void main() {
//	int num, rev;
//	scanf("%d", &num);	// 123
//	rev = reverse(num);
//	if (num == rev)
//	   printf("Palindrome");
//	else 
//	   printf("Not Palindrome");
//}
