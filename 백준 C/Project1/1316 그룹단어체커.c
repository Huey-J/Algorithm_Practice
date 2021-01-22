#include<stdio.h>
#include<string.h>

int main() {
	char str[101];
	int i, j, k, N, cnt = 0, str_length, is_groupSetence, flag;

	// 입력받을 문자열 개수
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%s", str);
		str_length = strlen(str);

		is_groupSetence = 1;	// 그룹단어 ( 1:true, 0:false )
		for (j = 0; j < str_length; j++) {
			// 현재 글자에 대한 flag
			flag = 0;
			for (k = j; k < str_length; k++) {
				// 해당 글자 다음으로 다른 글자가 나오면 flag=1로 변경
				if (str[j] != str[k]) flag = 1;

				// 이미 다른 글자가 나왔는데 다시 현재 글자가 나오면 그룹단어가 아님
				if (flag == 1 && str[j] == str[k]) {
					is_groupSetence = 0;
				}
			}
		}
		if (is_groupSetence == 1) cnt++;
	}
	printf("%d", cnt);

	return 0;
}