// 프로그래머스 카카오프렌즈 컬러링북 (210628)
// https://programmers.co.kr/learn/courses/30/lessons/1829
import java.util.ArrayList;
import java.util.Collections;
class Solution {
    int [][] visited;
    ArrayList<Integer> area = new ArrayList<Integer>();

    int row = 0;
    int col = 0;
    int localArea = 0;

    public void newPosition(int m, int n, int [][] picture) {
        int i = 0;
        int j = 0;
        Loop1 :
        for(i = 0; i < m; i++) {
            Loop2 :
            for(j = 0; j < n; j++) {
                if(visited[i][j] == 0 && picture[i][j] != 0) {
                    //System.out.println("newPosition : " + i + "," + j);
                    break Loop1;
                }
            }
        }

        row = i;
        col = j;
    }

    public void check(int m, int n, int [][] picture, int i, int j) {
        //System.out.println(i + "," + j);

        if(i == m && j == n) {
            //System.out.println("BasePoint");
            return;
        }

        if(picture[i][j] == 0) {
            localArea = 0;
            newPosition(m, n, picture);
            check(m, n, picture, row, col);
        }

        visited[i][j] = 1;
        localArea++;

        if(i != 0) {
            // 상
            if(visited[i-1][j] == 0 && picture[i-1][j] == picture[i][j]) {
                check(m, n, picture, i-1, j);
            }
        }

        if(i != m-1) {
            // 하
            if(visited[i+1][j] == 0 && picture[i+1][j] == picture[i][j]) {
                check(m, n, picture, i+1, j);
            }
        }

        if(j != 0) {
            // 좌
            if(visited[i][j-1] == 0 && picture[i][j-1] == picture[i][j]) {
                check(m, n, picture, i, j-1);
            }
        }

        if(j != n-1) {
            // 우
            if(visited[i][j+1] == 0 && picture[i][j+1] == picture[i][j]) {
                check(m, n, picture, i, j+1);
            }
        }

        // 재귀가 끝났을 때
        if(i == row && j == col) {
            area.add(localArea);
            localArea = 0;

            newPosition(m, n, picture);
            //System.out.println("newPoint : " + row + "," + col);
            check(m, n, picture, row, col);
        }
    }

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        visited = new int[m][n];

        check(m, n, picture, 0, 0);

        // for(int i = 0; i < m; i++) {
        //     for(int j = 0; j < n; j++) {
        //         //System.out.print(visited[i][j] + " ");
        //     }
        //     //System.out.println();
        // }

        for(int i = 0; i < area.size(); i++) {
            System.out.print(area.get(i) + " ");
        }

        //System.out.println("영역개수 : " + area.size());
        Collections.sort(area, Collections.reverseOrder());
        //System.out.println("최대영역 : " + area.get(0));


        int[] answer = new int[2];
        answer[0] = area.size();
        answer[1] = area.get(0);
        return answer;
    }
}