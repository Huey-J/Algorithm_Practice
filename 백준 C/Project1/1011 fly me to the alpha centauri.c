#include<stdio.h>
int main() {
	int i, N;
	/*
		�������� �� +1
		�����ٰ� ������ �߰����� +1

		9 ~ 16����
		9<x && x<16 - (16-9)/2
	*/

	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		long x, y;
		long long distance, k = 1;

		scanf("%ld%ld", &x, &y);

		distance = y - x;
		while (1) {
			if (distance <= k * k) { break; }
			k++;
		}

		//(k-1)*(k-1) < distance < k*k
		
		if (distance < k * k - (k * k - (k - 1) * (k - 1)) / 2) {
			printf("%ld\n", (k - 1) * 2);
		}
		else {
			printf("%ld\n", (k - 1) * 2 + 1);
		}
	}

	return 0;
}