import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class CountingValleys {

    static int countingValleys(int n, String s) {
        int valleysCount = 0;
        char[] path = s.toCharArray();
        int steps = 0;
        boolean isLastStepNegative=false;
        for (char d : path) {
            if (d == 'U') {
                if (steps < 0) {
                    isLastStepNegative = true;
                } else{
                    isLastStepNegative = false;
                }
                steps++;
            } else if (d == 'D'){
                if (steps < 0) {
                    isLastStepNegative = true;
                } else{
                    isLastStepNegative = false;
                }
                steps--;
            }
            if (steps == 0 && isLastStepNegative) {
                valleysCount++;
            }
        }
        return valleysCount;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String s = scanner.nextLine();

        int result = countingValleys(n, s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
