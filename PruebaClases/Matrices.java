package PruebaClases;

public class Matrices{
    
    public static void Mshow(double A[][]){
        
        byte n = (byte) A.length;
        
        for (byte i = 0; i < n; i++){
            
            System.out.println("");
            
            for(byte j = 0 ; j < n; j++){
            
                System.out.print(A[i][j]+" ");
                
            }
        }
        //return 0;
       }
       
       public static void MMult(double A[][], double B[][]){
        
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
           Mshow(C);
       }
       
       public static void main(String[] args){
           
           double A[][] = {{150,120},{150,120}};
           
           Mshow(A);
           
           double B[][] = {{2,0},{0,2}}; // 2*I2
           
           MMult(A,B);
           
           //MMult(B);
        
        }


}
