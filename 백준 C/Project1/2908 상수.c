#include<stdio.h>
#include<string.h>

int main() {
	char str1[10000], str2[1000];
	int A = 0, B = 0, i, input_str_length = 0, cnt = 1;

	// A�Է� �� ����
	scanf("%s", str1);
	input_str_length = strlen(str1);
	for (i = 0; i < input_str_length; i++) {
		B += (str1[i] - 48) * cnt;
		cnt *= 10;
	}

	cnt = 1;

	// B�Է� �� ����
	scanf("%s", str2);
	input_str_length = strlen(str2);
	for (i = 0; i < input_str_length; i++) {
		A += (str2[i] - 48) * cnt;
		cnt *= 10;
	}

	// ū �� ���
	printf("%d", A > B ? A : B);
	return 0;
}