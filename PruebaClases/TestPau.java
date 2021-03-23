 


/**
 * Write a description of class TestPau here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class TestPau {
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class TestPau
     */
    public TestPau(int a) {
        // initialise instance variables
        this.x = a;
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y
     */
    public int sampleMethod(int y) {
        // put your code here
        return x + y;
    }
    
    public static void main (String args[]){
    
        int t = 0;
        
        switch(t){
        
            case 0: System.out.println("CASE 0");
            case 1: System.out.println("CASE 1");
            case 2: System.out.println("CASE 2");
        }
        
        TestPau patata = new TestPau(2);
        int suma = patata.sampleMethod(3);
        int suma2 = patata.sampleMethod(2);
        
        System.out.println(suma);
    }
}
