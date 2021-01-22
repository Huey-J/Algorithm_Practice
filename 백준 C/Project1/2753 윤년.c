#include<stdio.h>
int main(void) {
	int a;

	scanf("%d", &a);

	//400의 배수이면 윤년
	if (a % 400 == 0) {
		printf("1");
		return 0;
	}

	//4의 배수이면서 100의 배수가 아니면 윤년
	if (a % 4 == 0 && a % 100 != 0) {
		printf("1");
		return 0;
	}

	// 모두 아니면 평년
	printf("0");
	return 0;
}