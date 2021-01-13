#include<stdio.h>

int getNumber(int a, int b) {
	if (a == 0 && b == 1) {
		return 1;
	}
	else if (a == 0 && b != 1) {
		return b;
	}
	else if (a != 0 && b == 1) {
		return getNumber(a - 1, b);
	}
	else {
		return getNumber(a - 1, b) + getNumber(a, b - 1);
	}
}

int main() {
	int T, result;
	int i;

	scanf("%d", &T);

	for (i = 0; i < T; i++) {
		int k, n;

		scanf("%d%d", &k, &n);

		result = getNumber(k, n);
		printf("%d\n", result);
	}

	return 0;
}