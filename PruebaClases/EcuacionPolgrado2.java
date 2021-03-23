 
//import Matrices.*;


public class EcuacionPolgrado2 {

    public static String EcuacionPolgrado2_3Puntos(Point p1, Point p2, Point p3) {
        
        double x1 = p1.getX();
        double x2 = p2.getX();
        double x3 = p3.getX();
        
        double y1 = p1.getY();
        double y2 = p2.getY();
        double y3 = p3.getY();
        
        double X[][] = {{x1*x1, x1, 1},{x2*x2, x2, 1},{x3*x3, x3, 1}};
        double Y[][] = {{y1},{y2},{y3}};
        double Xinv[][] = Matrices.MInverse3(X);
        
        double Mres[][] = (Matrices.MMult(Xinv, Y));
        
        double a,b, c;
        a = Mres[0][0];
        b = Mres[1][0];
        c = Mres[2][0];
        
        return a +"x2 + " + b + "x" + " + " + c;
    }
    
    public static String EcuacionPolGrado2_2Puntos(Point M, Point A){
    
        double x1 = M.getX();
        double x2 = A.getX();
        
        double y1 = M.getY();
        double y2 = A.getY();
        
        double a = -(y1-y2)/((x1-x2)*(x1-x2));
        double b = (2*x1*(y1-y2))/((x1-x2)*(x1-x2));
        double c = -(2*x1*x2*y1 - x2*x2*y1 - x1*x1*y2) / ((x1-x2)*(x1-x2));
        
    return a +"x2 + " + b + "x" + " + " + c;
    }

    public static void main (String args[]){
        
        Point p1 = new Point(0,1);
        Point p2 = new Point(1,10);
        Point p3 = new Point(2,33);
        Point Delta = new Point(-0.142856, 0.8571429);
        
        System.out.println(EcuacionPolgrado2_3Puntos(p1,p2,p3));
        System.out.println(EcuacionPolGrado2_2Puntos(Delta, p1));
    }
}
