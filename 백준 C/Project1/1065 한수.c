#include< stdio.h>

int han(int max) {
	int i, cnt = 0, tmp, now_diff, before_diff, flag;

	for (i = 1; i <= max; i++) {
		// ���ڸ��� ������ ���ڴ� ������������ �Ǻ��Ҽ� ���� ������ ������ �Ѽ�
		if (i < 100) {
			cnt++;
			continue;
		}

		tmp = i; flag = -1;
		now_diff = 0; before_diff = 0;
		while (1) {
			// 10���� ������ ��� (�Ѽ�)
			if (tmp < 10) break;

			// ������ 1���ڸ��� 10���ڸ��� ���� ���
			now_diff = tmp % 10;
			tmp /= 10;
			now_diff = now_diff - (tmp % 10);

			// ù��° �õ��� �Ѿ�� ���� �õ����� ���̰� �ٸ��� break (�Ѽ� �ƴ�)
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