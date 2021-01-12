#include<stdio.h>

int main() {
	int T, H, W, N;
	int i, result;

	scanf("%d", &T);

	// T만큼 테스트
	for (i = 0; i < T; i++) {
		scanf("%d %d %d", &H, &W, &N);

		// 가장 높은 층
		if (N % H == 0) {
			result = N / H;
			result += H * 100;
		}
		else {
			result = N / H + 1;
			result += (N % H) * 100;
		}
		printf("%d\n", result);
	}

	return 0;
}