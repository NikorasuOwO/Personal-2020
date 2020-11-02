package PruebaClases;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;



public class DeclaracionClases {
    
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
        
        return "y = " + a + "x" + " +" + b;
    }
    
    public static void main(String[] args){
    //int x = 1;
    //System.out.println(x);
        double point_xP = Integer.parseInt(JOptionPane.showInputDialog("coordenada x para P: "));
        double point_yP = Integer.parseInt(JOptionPane.showInputDialog("coordenada y para P: "));
        System.out.println("PUNTO P:" + point_xP + ";" + point_yP);
        
        Point P = new Point(point_xP, point_yP);
        
        int point_xQ = Integer.parseInt(JOptionPane.showInputDialog("coordenada x para Q: "));
        int point_yQ = Integer.parseInt(JOptionPane.showInputDialog("coordenada y para Q: "));
        System.out.println("\nPUNTO Q:" + point_xQ + ";" + point_yQ);
        
        Point Q = new Point(point_xQ, point_yQ);
        
        System.out.println(ecrectalineal(P,Q));
        
        
    }
    
    
}
