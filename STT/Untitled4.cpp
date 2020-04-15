#include<stdio.h>
void towers(int ,char ,char ,char );
int main()
{
	int n=2;
	towers(n,'A','B','C');
	return 0;
}

void towers(int n,char from,char aux,char to)
{
	if(n==1)
	{
		printf("move %d disk from %c using %c as aux\n",n,from,to,aux);
		return;
	}
	else
	{
		towers(n-1,from,to,aux);
		printf("move %d disk from %c using %c as aux\n",n,from,to,aux);
		towers(n-1,aux,to,from);
		return;
	}
}
