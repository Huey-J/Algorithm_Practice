#include<stdio.h>
int main(void) {
	int n, score;
	int i, j, last;
	char ox[80] = { 'a' };

	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%s", ox);
		
		last = 1;
		score = 0;
		for(j=0; j<80; j++) {
			if (ox[j] == 'O') {
				score += last++;
			}
			else if (ox[j] == 'X') {
				last = 1;
			}
			else {
				break;
			}
		}
		printf("%d\n", score);
		
		for (j = 0; j < 80; j++) {
			ox[j] = 'a';
		}
	}

	return 0;
}