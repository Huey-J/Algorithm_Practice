#include<stdio.h>
int main(void) {
	int n, i, M = 0;
	int arr[1000];
	double average, sum = 0;

	// ������ �Է�
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	// �ִ밪 M
	for (i = 0; i < n; i++) {
		if (M < arr[i]) M = arr[i];
	}

	for (i = 0; i < n; i++) {
		sum += (double)arr[i] / (double)M * 100.0;
	}
	printf("%lf", sum / (double)n);

	return 0;
}