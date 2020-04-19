#include<stdio.h>
#include<stdlib.h>
struct Student {
	char name[100];
	int marks;
};

struct Student * max(int n, struct Student *std) {
	int i, max=0;
	struct Student *res;
	res->marks = 0;
	for(i = 0; i < n; i++) {
		if (std[i].marks > res->marks) {
			res->marks = std[i].marks;
			strcpy(res->name,std[i].name);
		}
	}
	return res;
}

int main() {
	int i, n;
	scanf("%d",&n);
	struct Student *std, *res;
	std = (struct Student *)malloc(n*sizeof(struct Student));
	for(i = 0; i < n; i++) {
		scanf("%s %d",std[i].name, &std[i].marks);
	}
	printf("\n------------ Student Details ------------\nID\tNAME\t\tMARKS\n");
	for(i = 0; i < n; i++) {
		printf("%d\t%s\t\t%d\n", i+1, std[i].name, std[i].marks);
	}
	res = max(n, std);
	printf("\n------------ Student Having Maximum Marks ------------\n%s\t\t%d\n", res->name, res->marks);
	return 0;
}

//5
//Prasad 34
//Surya 50
//Aditya 40
//Suresh 44
//Mouli 30



