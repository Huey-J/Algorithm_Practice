#include<stdio.h>
int main() {
	int n;
	int i, j, min;

	scanf("%d", &n);

	min = 10000;

	for (i = 0; i < n / 3 + 1; i++) {
		for (j = 0; j < n / 5 + 1; j++) {
			if (3 * i + j * 5 == n && i+j<min) {
				min = i + j;
			}
		}
	}
	
	if (min == 10000) printf("-1\n");
	else printf("%d", min);
	 
	return 0;
}