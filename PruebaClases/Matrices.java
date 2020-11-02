package PruebaClases;

public class Matrices{
    
    private double A[][];
    
    public Matrices(double A[][]){
        
        this.A = A;
        
    }
        
    public void Mshow(){
        
        byte n = (byte) this.A.length;
        
        for (byte i = 0; i < n; i++){
            
            System.out.println("");
            
            for(byte j = 0 ; j < n; j++){
            
                System.out.print(this.A[i][j]+" ");
                
            }
        }
        //return 0;
       }
       
       public void MMult(double B[][]){
        
           //A es una matriz na x ma //B es una matriz nb x mb
           int na = A.length;
           int ma = A[0].length;
           int nb = B.length;
           int mb = B[0].length;
           
           double [][] C = new double[ma][nb];
           
           for (byte i = 0; i < na; i++){
            
            for(byte j = 0 ; j < mb; j++){
            
                for (byte k = 0 ; k < ma ; k++){
                    
                    C[i][j]= C[i][j] + A[i][k] * B[k][j]; //no entiendo este puto algoritmo :(
                
                }
                
            }
        }
           Matrices Cm = new Matrices(C);
           Cm.Mshow();
       }
       
       public static void main(String[] args){
           
           double A[][] = {{150,120},{150,120}};
           
           Matrices Am = new Matrices(A);
           Am.Mshow();
           
           double B[][] = {{2,0},{0,2}};
           
           Am.MMult(B);
           
           //MMult(B);
        
        }


}
