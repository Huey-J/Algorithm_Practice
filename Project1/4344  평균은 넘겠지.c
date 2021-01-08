#include<stdio.h>

int main(void) {
	int n_case, n_student;
	int i, j, total, cnt;
	int score[1001];
	double average;

	scanf("%d", &n_case);

	for (i = 0; i < n_case; i++) {
		total = 0;
		cnt = 0;
		scanf("%d", &n_student);

		for (j = 0; j < n_student; j++) {
			scanf("%d", &score[j]);
			total += score[j];
		}

		average = (double)total / (double)n_student;
		
		for (j = 0; j < n_student; j++) {
			if (average < score[j])
				cnt++;
		}

		printf("%.3lf%%\n", (double)cnt / (double)n_student * 100.0);
	}

	return 0;
}