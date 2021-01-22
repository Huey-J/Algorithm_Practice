#include<stdio.h>

void printSelfNumber() {
	int i, sum, n;
	int arr[10001] = { 0 };

	for (i = 1; i <= 10000; i++) {
		sum = i, n = i;

		while (1) {
			// exit: ���� ���� 0�� ��� (��� �ڸ��� ���ڸ� ����)
			if (n == 0) break;

			sum += n % 10;	// ������ 1���ڸ� ���ϱ�
			n /= 10;		// ������ 1���ڸ� ���ֱ�
		}

		// index overflow �����ϸ鼭 arr ����
		if(sum <= 10000) arr[sum]++;
	}

	// ���
	for (i = 1; i < 10000; i++) {
		if (arr[i] == 0) printf("%d\n", i);
	}
}

int main(void) {
	printSelfNumber();
	return 0;
}