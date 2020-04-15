#include <stdio.h>
struct employee
{
	int eno;
	char ename[20];
	float esalary;
};
int main()
{
	struct employee e,*e1;
	printf("Enter employee no:\t");
	scanf("%d",&e.eno);
	printf("Enter employee name:\t");
	scanf("%s",&e.ename);
	printf("Enter salary:\t");
	scanf("%f",&e.esalary);
	printf("Eno:\t%d",e.eno);
	printf("\nEname:\t%s",e.ename);
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
