package 프로그래머스LV1;

public class 구현_숫자짝궁 {

  public String solution(String X, String Y) {
    // 입력 문자열의 각 문자의 빈도를 저장할 배열
    int[] countX = new int[10];
    int[] countY = new int[10];

    // X와 Y의 각 문자의 빈도를 계산
    for (char c : X.toCharArray()) {
      countX[c - '0']++;
    }

    for (char c : Y.toCharArray()) {
      countY[c - '0']++;
    }

    // 공통으로 존재하는 숫자를 찾고 큰 숫자부터 결과를 생성
    StringBuilder result = new StringBuilder();

    for (int i = 9; i >= 0; i--) {
      int commonCount = Math.min(countX[i], countY[i]);
      for (int j = 0; j < commonCount; j++) {
        result.append(i);
      }
    }

    // 결과가 빈 문자열인 경우 -1 반환
    if (result.length() == 0) {
      return "-1";
    }

    // 결과가 0으로만 구성된 경우 0 반환
    if (result.toString().matches("0+")) {
      return "0";
    }

    return result.toString();
  }

  public static void main(String[] args) {
    구현_숫자짝궁 test = new 구현_숫자짝궁();
    System.out.println(test.solution("100", "2345")); // -1
    System.out.println(test.solution("100", "203045")); // 0
    System.out.println(test.solution("100", "123450")); // 10
    System.out.println(test.solution("12321", "42531")); // 321
    System.out.println(test.solution("5525", "1255")); // 552
  }
}
