#include<stdio.h>
#include<string.h>

int main() {
	char str[101];
	int i, j, k, N, cnt = 0, str_length, is_groupSetence, flag;

	// �Է¹��� ���ڿ� ����
	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%s", str);
		str_length = strlen(str);

		is_groupSetence = 1;	// �׷�ܾ� ( 1:true, 0:false )
		for (j = 0; j < str_length; j++) {
			// ���� ���ڿ� ���� flag
			flag = 0;
			for (k = j; k < str_length; k++) {
				// �ش� ���� �������� �ٸ� ���ڰ� ������ flag=1�� ����
				if (str[j] != str[k]) flag = 1;

				// �̹� �ٸ� ���ڰ� ���Դµ� �ٽ� ���� ���ڰ� ������ �׷�ܾ �ƴ�
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