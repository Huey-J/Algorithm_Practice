#include<stdio.h>
int main(void) {
	int n, max = -1000000, min = 1000000, tmp, i;

	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d", &tmp);

		if (tmp > max) max = tmp;
		if (tmp < min) min = tmp;
	}
	printf("%d %d\n", min, max);
	return 0;
}