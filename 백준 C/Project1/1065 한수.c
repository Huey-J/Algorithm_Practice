#include< stdio.h>

int han(int max) {
	int i, cnt = 0, tmp, now_diff, before_diff, flag;

	for (i = 1; i <= max; i++) {
		// 세자리수 이하의 숫자는 등차수열인지 판별할수 없기 때문에 무조건 한수
		if (i < 100) {
			cnt++;
			continue;
		}

		tmp = i; flag = -1;
		now_diff = 0; before_diff = 0;
		while (1) {
			// 10보다 작으면 통과 (한수)
			if (tmp < 10) break;

			// 현재의 1의자리와 10의자리의 차이 계산
			now_diff = tmp % 10;
			tmp /= 10;
			now_diff = now_diff - (tmp % 10);

			// 첫번째 시도는 넘어가고 다음 시도부터 차이가 다르면 break (한수 아님)
			if (flag == -1) { flag = 0; }
			else if (before_diff != now_diff) {
				flag++;
				break;
			}
			before_diff = now_diff;
		}

		if (flag == 0) cnt++;
	}

	return cnt;
}

int main(void) {
	int input;

	scanf("%d", &input);
	printf("%d", han(input));

	return 0;
}