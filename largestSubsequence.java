import java.io.*;
import java.util.*;

class largestSubsequence {
    public static int Subsequence(String str1, String str2) {
        int m = str1.length(), n = str2.length();
        int[][] dp = new int[m + 1][n + 1];
        for(int i = 1; i <= m; i++)
            for(int j = 1; j <= n; j++)
                if(str1.charAt(i-1) == str2.charAt(j-1)) dp[i][j] = dp[i-1][j-1] + 1;
                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        return dp[m][n];
    }
    public static void main(String[] args) throws IOException{
        Scanner sc=new Scanner(System.in);

        System.out.println("Enter String 1 : ");
        String str1=sc.nextLine();
        
        System.out.println("Enter String 2 : ");
        String str2=sc.nextLine();
        int sub=Subsequence(str1,str2);
        System.out.println(sub);
        sc.close();
    }
}