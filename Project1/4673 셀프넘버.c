#include<stdio.h>

void printSelfNumber() {
	int i, sum, n;
	int arr[10001] = { 0 };

	for (i = 1; i <= 10000; i++) {
		sum = i, n = i;

		while (1) {
			// exit: 더할 값이 0일 경우 (모든 자리의 숫자를 더함)
			if (n == 0) break;

			sum += n % 10;	// 현재의 1의자리 더하기
			n /= 10;		// 현재의 1의자리 없애기
		}

		// index overflow 방지하면서 arr 변경
		if(sum <= 10000) arr[sum]++;
	}

	// 출력
	for (i = 1; i < 10000; i++) {
		if (arr[i] == 0) printf("%d\n", i);
	}
}

int main(void) {
	printSelfNumber();
	return 0;
}