#include<stdio.h>
//#include<stdlib.h>
//int* fib(int n) {
//	int a = 0, b = 1, c = 0, i, *res;
//	res = (int *)malloc(n*sizeof(int));
//	for(i = 0; i < n; i++) {
//		if (i==0) 
//			res[i]=a;
//		else if(i==1)
//			res[i]=b;
//		else {
//			c = a + b;
//			res[i] = c;
////			printf("%d ",c);
//			a = b;
//			b = c;
//		}
//	}
//	return res;
//}
//int main() {
//	int n, *fibb, i;
//	scanf("%d",&n);
//	fibb = fib(n);
//	for(i = 0; i < n; i++) {
//		printf("%d ",*(fibb+i));
//	}
//	return 0;
//}
int main()
{
   int a[5],i=0;
   while(i<5)
    a[i]=++i;
   for(i=0;i<5;i++)
    printf("%d",a[i]);
   return 0;
}
