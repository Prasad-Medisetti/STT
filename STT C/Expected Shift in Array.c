
#include<stdio.h>
int main()
{
	int n, i, shift, key, loc;
	printf("Enter no.of elements:\n");
    scanf("%d", &n);
	int a[n];
	printf("Enter elements:\n");
	for(i = 0;i < n;i++)
		scanf("%d", &a[i]);
    printf("Enter the element to find its location after shifting:\n");
    scanf("%d", &key);
	printf("Enter Shift:\n");
    scanf("%d", &shift);
    for(i = 0;i < n;i++)
    {
    	if(a[i] == key)
    		break;
    	else  if(i == n-1)
    	{
		    printf("Element not found");
    	   	return;
		}
	}
	printf("%d is at %d location after shifting", key, (shift + i) % n + 1);
	printf("\nEnter the location to find its element after shifting:\n");
	scanf("%d", &loc);
   	printf("%d is at %d location after shifting", ((n-shift%n)+loc)%n, loc);
    return 0;
}
