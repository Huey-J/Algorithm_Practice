#include<stdio.h>
int main(void) {
	int input, result, cnt = 0;

	scanf("%d", &input);

	result = input;
	while (1) {
		result = ((result / 10) + (result % 10)) % 10 + (result % 10) * 10;
		cnt++;

		if (result == input) {
			break;
		}
	}
	printf("%d", cnt);

	return 0;
}