#include<stdio.h>
int main(void) {
	int a;

	scanf("%d", &a);

	//400�� ����̸� ����
	if (a % 400 == 0) {
		printf("1");
		return 0;
	}

	//4�� ����̸鼭 100�� ����� �ƴϸ� ����
	if (a % 4 == 0 && a % 100 != 0) {
		printf("1");
		return 0;
	}

	// ��� �ƴϸ� ���
	printf("0");
	return 0;
}