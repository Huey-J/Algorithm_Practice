#include<stdio.h>
int sum(int* arr, int n) {
	int sum = 0, i;
	for (i = 0; i < n; i++) {
		sum += arr[i];
	}
	return sum;
}

int main(void) {
	int n, i, arr[300];

	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	printf("%d", sum(arr, n));
	return 0;
}