#include<stdio.h>
#include<string.h>
int main() {
	char a[10001], b[10001], result[10001];
	int i, j, cnt, tmp, upper;

	scanf("%s%s", a, b);

	i = strlen(a) - 1;
	j = strlen(b) - 1;
	cnt = 0;
	upper = 0;

	while (1) {
		if (i < 0 && j < 0) { break; }

		if (i < 0 && j >= 0) {
			tmp = b[j] - '0';	//b[j]�� ���ϱ�
		}
		else if (j < 0 && i >= 0) {
			tmp = a[i] - '0';	//a[i]�� ���ϱ�
		}
		else {
			tmp = a[i] - '0' + b[j] - '0';
		}

		// �ø�ó��
		if (upper == 1) { tmp++; }
		if (tmp > 9) { upper = 1; }
		else { upper = 0; }

		result[cnt] = tmp % 10 + '0';

		cnt++;
		i--;
		j--;
	}

	// ������ ���� �ø�
	if (upper == 1) {
		result[cnt] = 1 + '0';
		cnt++;
	}

	for (i = cnt - 1; i >= 0; i--)
		printf("%c", result[i]);	// ���
	
	return 0;
}