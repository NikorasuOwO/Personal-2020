 

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;



public class EcuacionRecta {
    
    public static String ecrectalineal(Point P, Point Q){
        
        // y = ax + b
        //El vector PQ tiene como coordenadas pqx y pqy
        
        double Px = P.getX();
        double Py = P.getY();
        double Qx = Q.getX();
        double Qy = Q.getY();
        
        double pqx = Qx - Px;
        double pqy = Qy - Py;
        
        double a = pqy/pqx;
        double b = Py - ((pqy*Px)/pqx);
        
        String res = new String("y = ");
       // System.out.print(a + "x"+ " + " + b);
        
        if(a == 0.0) {;}
        if(a == 1.0) {
            res = res + "x ";
        }
        if (a == -1.0) {
            res = res + "-x ";
                }
        if (a != 0.0 && a != 1.0 && a != -1.0){
            res = res + a + "x ";}
            
        if (b > 0) {
            if (a == 0){
                res = res + b;
            }else{
                res = res + "+ " + b;
            }
        }
        
        if (b < 0) {
            if (a == 0){
                res = res + b;
            }else{
                res = res + "- " + Math.abs(b);
            }
        }
        if (a == 0.0 && b == 0.0){
            res = res + 0;
        }
        return res;
        }


    
    public static void main(String[] args){
    //int x = 1;
    //System.out.println(x);
        double point_xP = Integer.parseInt(JOptionPane.showInputDialog("coordenada x para P: "));
        double point_yP = Integer.parseInt(JOptionPane.showInputDialog("coordenada y para P: "));
        System.out.println("PUNTO P:" + "("+ point_xP + ";" + point_yP + ")");
        
        Point P = new Point(point_xP, point_yP);
        
        int point_xQ = Integer.parseInt(JOptionPane.showInputDialog("coordenada x para Q: "));
        int point_yQ = Integer.parseInt(JOptionPane.showInputDialog("coordenada y para Q: "));
        System.out.println("\nPUNTO Q:" + "("+ point_xQ + ";" + point_yQ + ")");
        
        Point Q = new Point(point_xQ, point_yQ);
        
        System.out.println("\n" + ecrectalineal(P,Q));
        
        
    }
}
    
