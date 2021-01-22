#include<stdio.h>

int main() {
	long A, B, C, n = 0;

	scanf("%d%d%d", &A, &B, &C);

	//아래 방식처럼 공식대로 푸는 것이 아니라 수학적 사고능력이 필요함
	//while (1) {
	//	n++;
	//	// 손익분기점
	//	if (A + B * n < C * n) {
	//		printf("%d", n);
	//		break;
	//	}
	//	// 존재 X
	//	if (n > 10000000) {
	//		printf("-1");
	//		break;
	//	}
	//}


	/*
		A+Bn < Cn		<- 이 공식이 성립되는 첫번째 n을 찾으면 된다.
		A < (C-B)n
		A/(C-B) < n		<- n은 횟수이므로 자연수이기 때문에
							A/(C-B)보다 최소 1이 더 크면 식이 성립한다.
							B가 C보다 크거나 같으면 자연수 n보다 클 수 없다.
	*/

	if (B >= C) {
		printf("-1");
	}
	else {
		printf("%d", A / (C - B) + 1);
	}
	return 0;
}