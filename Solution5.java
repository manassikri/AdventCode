package Advent30Days;

import java.io.File;
import java.io.FileReader;
import java.util.Scanner;

public class Solution5 {
    public static void main(String[] args) throws Exception {
        File fl = new File("D:\\DownloadsD\\PythonPrograms\\AdventCode\\text5.txt");
        Scanner scn = new Scanner(fl);
        int max = Integer.MIN_VALUE;
        while (scn.hasNextLine()) {
            max = Math.max(max, calculateValue(scn.nextLine()));
        }
        System.out.println(max);
    }

    public static int calculateValue(String str) {


        int l = 0;
        int r = 127;

        for (int i = 0; i < 7; i++) {
            char ch = str.charAt(i);

            if (ch == 'F') {

                int m = (l + r) / 2;
                r = m;

            } else {
                int m = (l + r) / 2;
                l = m + 1;
            }

        }

        int row = l;
        l = 0;
        r = 7;

        for (int i = 7; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch == 'L') {

                int m = (l + r) / 2;
                r = m;

            } else {
                int m = (l + r) / 2;
                l = m + 1;
            }
        }
        int col = l;


        return row * 8 + col;
    }
}
