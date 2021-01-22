#include<stdio.h>
int main(void) {
	int hour, min;
	int temp_hour = 24, temp_min = 0;

	scanf("%d%d", &hour, &min);

	temp_hour += hour;
	temp_min += min;

	temp_min -= 45;

	if (temp_min < 0) {
		temp_min += 60;
		temp_hour--;
	}
	temp_hour %= 24;

	printf("%d %d", temp_hour, temp_min);
	

	return 0;
}