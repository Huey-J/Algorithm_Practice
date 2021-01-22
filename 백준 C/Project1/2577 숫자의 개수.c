#include<stdio.h>
int main(void) {
	int a, b, c, result, tmp, i;
	int arr[10] = { 0 };

	scanf("%d%d%d", &a, &b, &c);

	result = a * b * c;

	while (result > 0) {
		tmp = result % 10;
		arr[tmp]++;

		result /= 10;
	}

	for (i = 0; i < 10; i++) {
		printf("%d\n", arr[i]);
	}

	return 0;
}