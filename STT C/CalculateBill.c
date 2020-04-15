/*
2.	Food Corner home delivers vegetarian and non-vegetarian combos to its customer based on order. 
	A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate.
	Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than 
	the vegetarian combo.
	Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. The delivery charges are as mentioned below:
	Distance in kms		Delivery charge in Rs per km
	For first 3kms		0
	For next 3kms		3
	For the remaining	6
	Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery 
	point, write a C program to calculate the final bill amount to be paid by a customer. 
	The below information must be used to check the validity of the data provided by the customer: 
	i.		Type of food must be 'V' for vegetarian and 'N' for non-vegetarian.
	ii.		Distance in kms must be greater than 0.
	iii.	Quantity ordered should be minimum 1.
	If any of the input is invalid, the bill amount should be considered as -1.
*/
#include <stdio.h>
int main()
{
	char FOOD;
	int distance,quantity,bill=-1,cost_V = 120, cost_N = 150;
	printf("Enter the type of FOOD(V for Veg/N for Non-Veg):\n");
	scanf("%c",&FOOD);
	printf("Enter Quantity of FOOD:\n");
	scanf("%d",&quantity);
	printf("Enter the Distance in kms from the restaurant to the delivery point:\n");
	scanf("%d",&distance);
	if(FOOD == 'V' && distance > 0 && quantity >= 1)
	{
		bill = quantity * cost_V;
	}
	else if(FOOD == 'N' && distance > 0 && quantity >= 1)
	{
		bill = quantity * cost_N;
	}
	else
	{
		bill = -1;
		printf("Bill :\tRs. %d ",bill);
		return 0;
	}
	int d = distance;
	d -= 3;
	while(d > 0)
	{
		if(d == distance-6)
		{
			d -= 3;
			bill += 3*3;
			continue;
		}	
		else
		{
			bill += 6;
			d--;
			continue;
		}
	}
	printf("Bill :\tRs. %d ",bill);
	return 0;
}
