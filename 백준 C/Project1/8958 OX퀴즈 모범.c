#include <stdio.h>
#include <string.h>

int main(void) {
	int n, i, j, sum, add; //sum = 최종적인 점수, add = 추가적으로 더해지는 점수
	char arr[81];

	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		sum = 0, add = 1;
		scanf("%s", arr);

		//strlen은 string.h파일에 있는 함수 중 문자열의 길이를 측정할 때 사용됨
		for (j = 0; j < strlen(arr); j++) {
			if (arr[j] == 'O') {
				sum += add;
				add++;
			}
			else {
				add = 1;
			}
		}
		printf("%d\n", sum);
	}
	return 0;
}
