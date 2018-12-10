import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class RepeatedString {

    static int getCount(String string) {
        int count = 0;
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == 'a') {
                count++;
            }
        }
        return count;
    }

    // Complete the repeatedString function below.
    static long repeatedString(String s, long n) {
        long occurance = 0l;
        int aCount = 0;
        if (s.length() < n) {
            aCount = getCount(s);
            occurance = (n / s.length()) * aCount;
            s = s.substring(0, (int) (n % s.length()));
            occurance += getCount(s);
        } else {
            s = s.substring(0, (int) n);
            occurance = getCount(s);
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
