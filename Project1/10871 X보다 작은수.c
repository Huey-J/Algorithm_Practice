#include<stdio.h>
int main(void) {
	int n, x, i, tmp;

	scanf("%d%d", &n, &x);

	for (i = 0; i < n; i++) {
		scanf("%d", &tmp);

		if (tmp < x) {
			printf("%d ", tmp);
		}
	}
	
	return 0;
}