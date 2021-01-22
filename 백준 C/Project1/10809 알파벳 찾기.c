#include<stdio.h>
#include <string.h>
int main(void) {
	char str[100];
	int i, arr[26];

	// 배열 초기화
	for (i = 0; i < 26; i++) {
		arr[i] = -1;
	}

	scanf("%s", str);
	for (i = 0; i < strlen(str); i++) {
		int alphabet_num;

		alphabet_num = str[i] - 97;
		if (arr[alphabet_num] == -1) {
			arr[alphabet_num] = i;
		}
	}

	for (i = 0; i < 26; i++) {
		printf("%d ", arr[i]);
	}

	return 0;
}