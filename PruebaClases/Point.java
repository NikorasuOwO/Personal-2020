package PruebaClases;


 

public class Point{
    
    private double x,y;
    
    public Point(double x, double y){
        this.x = x;
        this.y = y;
    }


    public double dist(Point q){
        
        double xq = q.getX();
        double yq = q.getY();
        
    return Math.sqrt(Math.pow(xq - this.x, 2) + Math.pow(yq - this.y, 2));
    }
    
    public double getX(){
        return x;
    }
    
    public double getY(){
        return y;
    }
    
    public void setX(double X) {
        this.x = X;
    }
    
    public void setY(double Y){
        this.y = Y;
    }
}