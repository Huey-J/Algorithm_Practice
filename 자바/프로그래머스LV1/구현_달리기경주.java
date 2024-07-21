package 프로그래머스LV1;

import java.util.*;

public class 구현_달리기경주 {
  public String[] solution(String[] players, String[] callings) {

    Map<String, Integer> rankingMap = new HashMap<>();

    for (int i=0; i<players.length; i++) {
      rankingMap.put(players[i], i);
    }

    for (String c : callings) {
      // find
      int index = rankingMap.get(c);

      // swap
      String swap = players[index];
      players[index] = players[index-1];
      players[index-1] = swap;

      // renew map
      rankingMap.put(players[index], index);
      rankingMap.put(players[index-1], index-1);
    }

    // for (String s : callings) {
    //     for (int i=0; i<players.length; i++) {
    //         if(players[i].equals(s)) {
    //             String swap = players[i];
    //             players[i] = players[i-1];
    //             players[i-1] = swap;
    //         }
    //     }
    // }

    return players;
  }

  public static void main(String[] args) {
    구현_달리기경주 test = new 구현_달리기경주();

    String[] result = test.solution(
        new String[]{"mumu", "soe", "poe", "kai", "mine"},
        new String[]{"kai", "kai", "mine", "mine"}
    );

    for (String s : result) {
      // ["mumu", "kai", "mine", "soe", "poe"]
      System.out.print(s + " ");
    }
  }
}
