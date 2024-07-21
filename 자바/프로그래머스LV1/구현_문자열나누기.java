 package 프로그래머스LV1;

public class 구현_문자열나누기 {

  public int solution(String s) {
    int answer = 0;

    int count_x = 0;
    int count_y = 0;

    char char_x = s.charAt(0);

    for (char c : s.toCharArray()) {
      if (count_x == 0) {
        char_x = c;
      }

      if (char_x == c) {
        count_x++;
      } else {
        count_y++;
      }

      if (count_x == count_y) {
        count_x = 0;
        count_y = 0;
        answer++;
      }
    }

    return answer;
  }

  public static void main(String[] args) {
    구현_문자열나누기 test = new 구현_문자열나누기();
    System.out.println(test.solution("banana")); //	3
    System.out.println(test.solution("abracadabra")); //	6
    System.out.println(test.solution("aaabbaccccabba")); //	3
  }

}
