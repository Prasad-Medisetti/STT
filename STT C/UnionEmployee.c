#include <stdio.h>
union employee
{
	int eno;
	char ename[20];
	float esalary;
};
int main()
{
	union employee e,*e1;
	printf("Enter employee no:\t");
	scanf("%d",&e.eno);
	printf("Eno:\t%d",e.eno);
	printf("\nEnter employee name:\t");
	scanf("%s",&e.ename);
	printf("Ename:\t%s",e.ename);
	printf("\nEnter salary:\t");
	scanf("%f",&e.esalary);
	printf("\nSalary:\t%f",e.esalary);
	printf("\nSizeof e:\t%d",sizeof(e));
	e1=&e;
	printf("\nEno:\t%d",e.eno);
	e.eno=20;
	printf("\nEno:\t%d",e1->eno);
	printf("\nSizeof e:\t%d",sizeof(e));
	printf("\nSizeof e1:\t%d",sizeof(e1));
	printf("\nAddress of e:\t%u",&e);
	printf("\nAddress of e1:\t%u",&e1);
	return 0;
}
