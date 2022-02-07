import java.util.Arrays;

public class FIRST {
    public static void main(String[] args) {
        // Step 1
        long a[];
        a = new long[16];
        a[0] = 3;
        for (int i = 1; i < a.length; i++) {
            a[i] = a[i - 1] + 1;
        }
        // Step 2
        float[] x = new float[13];
        for (int i = 0; i < x.length; i++) {
            x[i] = getRandomNumber(-4, 11);
        }
        //Step 3
        String[] h = {"3","5", "6", "8", "10", "14","15","17"};
        double[][] A = new double[16][13];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < x.length; j++) {
                if (a[i] == 16) {
                    A[i][j] = Math.tan(Math.sin(2*Math.pow(0.25-x[j],x[j])));
                } else if (in(h, String.valueOf(a[i]))) {
                    A[i][j] = Math.cbrt(Math.tan(Math.pow(Math.PI*(1-x[j]),3)));
                } else {
                    A[i][j] = Math.sin(Math.pow(1/(3*Math.pow(Math.E,Math.pow(0.5*x[j],2))),2));
                }
            }
        }
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < x.length; j++) {
                String formattedDouble = String.format("%.5f", A[i][j]);
                System.out.print(formattedDouble + " ");
            }
            System.out.println();
        }
    }

    public static boolean in(String[] arr, String targetValue) {
        return Arrays.asList(arr).contains(targetValue);
    }

    public static float getRandomNumber(float min, float max) {
        return (float) (Math.random() * (max - min)) + min;
    }
}
