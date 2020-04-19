//bit.ly/doubts_day1

#include<stdio.h>
int prime(int num1,int num2)
{
int i,j,pc=0;
for(i=num1;i<=num2;i++)
{
int count=0;
if(i==0||i==1)
{
count=1;
}
for(j=2;j<=i/2;j++)
{
if(i%j==0)
{
count++;
break;
}
}
if(count==0)
{
pc++;
}

}
return pc;
}
int main()
{
int num1,num2,t,i,result;
scanf("%d",&t);
for(i=1;i<=t;i++)
{
scanf("%d%d",&num1,&num2);
result=prime(num1,num2);
printf("%d",result);

}
}

#include<stdio.h>

//void main() {
//
//    int num, fc = 0;
//    scanf("%d",&num);   // 10
//    // num=10 1..100
//
//    // Direct Code
//    // for (int i = 1; i <= num; i++) {
//    //     if (num % i == 0) {
//    //         fc++;              
//    //     }
//    // }
//    // if (fc == 2) {
//    //     printf("Prime\n");
//    // }
//    // else {
//    //     printf("Not Prime\n");
//    // }
//    
//
//    // Using Function
//    fc = factors_count(num);    // Function Call
//    if (fc == 0) {
//        printf("Prime\n");
//    }
//    else {
//        printf("Not Prime\n");
//    }
//    
//}

// Using Function 
//int factors_count(num) {
//    int i, fc = 0;
//    if (num==0 || num==1) 
//        return 0;
//    for (i = 1; i <= num; i++) {
//        if (num%i==0)
//            fc++;
//    }
//    return fc;
//}

// Using Function 
//int factors_count(num) {
//    int i, fc = 0;
//    if (num==0 || num==1) 
//        return 1;
//    for (i = 2; i <= num/2; i++) {
//        if (num%i==0) {
//            fc++;
//			break;
//		}
//    }
//    return fc;
//}
//
//int main() {
//	 
//    int num, fc = 0, t,i;
//    scanf("%d",&t);   // 10
//    
//  	for (i = 1; i <= t; i++) {	// Test Cases Loop
//  		int num, fc = 0;
//    	scanf("%d",&num);
//  		
//	    // Using Function
//	    fc = factors_count(num);    // Function Call
//	    if (fc == 0) {
//	        printf("Prime\n");
//	    }
//	    else {
//	        printf("Not Prime\n");
//	    }
//	}
//	return;
//}
//
//



//3
//10 14
//20 25
//50 55
//2
//1 
//2
