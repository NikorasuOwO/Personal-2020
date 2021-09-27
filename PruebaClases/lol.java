package PruebaClases;


/**
 * Write a description of class lol here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class lol {
    // instance variables - replace the example below with your own
    public static double testMethod(double[] v, int left, int right) {
        if (left > right) { return 1.0; }
        else {
            int middle = (left + right) / 2;
            return v[middle]
                * testMethod(v, left, middle - 1)
                * testMethod(v, middle + 1, right);
        }
    }
}
