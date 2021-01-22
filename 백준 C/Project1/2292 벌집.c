#include<stdio.h>

int main() {
	int input_number, n = 0;

	scanf("%d", &input_number);

	// n:횟수
	// 2  <= n:2 <=7	6증가
	// 8  <= n:3 < 19	12증가
	// 20 <= n:4 < 37	18증가 (6의 등차수열)

	// 6*( n*(n+1)/2 ) + 2 <= n+2 <= 6*( (n+1)(n+2)/2 ) + 1

	if (input_number == 1) {
		printf("1");
		return 0;
	}

	while (1) {
		if (3 * n * (n + 1) + 2 <= input_number && input_number <= 3 * (n + 1) * (n + 2) + 1) {
			printf("%d", n + 2);
			break;
		}
		n++;
	}
	return 0;
}