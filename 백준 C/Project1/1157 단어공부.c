#include<stdio.h>
#include<string.h>

int main() {
	char str[1000001];
	int arr[26] = { 0 };
	int max = 0, max_index = 0, flag = 0, i, input_str_length = 0;

	// count 배열 생성
	scanf("%s", str);
	input_str_length = strlen(str);
	for (i = 0; i < input_str_length; i++) {
		// 소문자
		if ('a' <= str[i] && str[i] <= 'z') arr[str[i] - 97]++;
		// 대문자
		else arr[str[i] - 65]++;
	}

	// max 계산
	for (i = 0; i < 26; i++) {
		if (arr[i] > max) {
			max = arr[i];
			max_index = i;
			flag = 0;
		}
		else if (arr[i] == max) {
			flag = 1;
		}
	}

	// 결과 출력
	if (flag == 1) printf("?");
	else printf("%c", max_index + 65);

	return 0;
}