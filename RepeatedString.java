import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class RepeatedString {

    // Complete the repeatedString function below.
    static long repeatedString(String s, long n) {
        long occurance = 0l;
        int aCount = 0;
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        String sorted = new String(chars);
        for (int i = 0; i < sorted.length(); i++) {
            if (sorted.charAt(i) != 'a') {
                break;
            }
            aCount++;
        }
        System.out.println("String:" + s);
        if (s.length() < n) {
            System.out.println( n/s.length() * aCount + ",reminder"+ n%s.length());
        }
        return occurance;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        long n = scanner.nextLong();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        long result = repeatedString(s, n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
