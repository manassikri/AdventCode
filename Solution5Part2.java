package Advent30Days;

import java.io.File;
import java.io.FileReader;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Scanner;

public class Solution5Part2 {
    public static void main(String[] args) throws Exception {
        File fl = new File("D:\\DownloadsD\\PythonPrograms\\AdventCode\\text5.txt");

        HashSet<Integer> set = new HashSet<>();
        Scanner scn = new Scanner(fl);
        int max = Integer.MIN_VALUE;
        int count = 0;
        while (scn.hasNextLine()) {
            count++;
            int ret = calculateValue(scn.nextLine());
            //System.out.println(ret);
            if (ret == 859) {
                System.out.println(ret);
            }

            set.add(ret);
        }
        //System.out.println(count);
//        System.out.println(set.size());
//        for (int i : set) {
//            System.out.println(i);
//        }
        //System.out.println(max);
        for (int i = 0; i <= 127*8+7; i++) {

            if (set.contains(i - 1) && (!set.contains(i)) && set.contains(i + 1)) {
                System.out.println(i);
            }

        }
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
        int num = row * 8 + col;

        System.out.println(str + " ->" + num);
        return num;
    }
}
