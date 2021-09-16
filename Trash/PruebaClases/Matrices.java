 public class Matrices{
        
        public static void Mshow(double A[][]){
            
            byte n = (byte) A.length;
            byte m = (byte) A[0].length;
            System.out.println("");
            for (byte i = 0; i < n; i++){
                
                System.out.println("");
                
                for(byte j = 0 ; j < m; j++){
                
                    System.out.print(A[i][j]+" ");
                    
                }
            }
            System.out.println("");
           }
           
           public static double[][] MMultScalar(double A[][], double a){
            
            double[][]A2 = A;
            byte n = (byte) A.length;
            
            for (byte i = 0; i < n; i++){
                
                for(byte j = 0 ; j < n; j++){
                
                    A2[i][j] = a * A2[i][j];
                    
                }
            }
               return A2;
           }
           
           public static double[][] MMult(double A[][], double B[][]){
            
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
            return C;
            //Mshow(C);
           }
           
           public static double MDet2(double A[][]){
               if(2 == A.length){
               double Det = A[0][0]*A[1][1] - A[0][1]*A[1][0] ;
               return Det;
            }
            return -1234567;
            }
           public static double[] addArray(double[] a, double valor){
               
               double[] a2 = new double[a.length+1];
               a2[a.length] = valor;
               for(int i = 0 ; i < a.length; i++){a2[i] = a[i];}
               return a2;
           }
           
           public static boolean esta_en_array(int[]a, int v){
            
               for(int i = 0; i < a.length ; i++){
                   if(a[i] == v){return true;}
               }
               return false;
           }
           
           public static int Buscar(int[]a, int n){
           //Buscamos el entero de 0 a n que no pertece a "a".
           for(int i = 0; i < n; i++){
               if(!esta_en_array(a, i)){
                   return i;
               }else{;}
               
           }
           return 0;
           }
           
           public static double MDetN(double[][] A, int n, int[] rows, int[] cols){ //START: out = {}
               double r = 0;
               if(rows.length == n-1 && cols.length == n-1){ //BASE 1x1
                   //Bucsamos la linea que no hemos quitado
                   int row = Buscar(rows, n);
                   //Ahora buscamos columna
                   int col = Buscar(cols, n);
                   //System.out.println("row:" + row + "col:"+col);
                   return A[row][col];
               }else{
                   for(int i = 0 ; i < n ; i++){
                       
                       int sign = (int) Math.pow(-1, 1+(i+1));
                       r = r + A[0][i]*sign*MDetN();
                    
                   }
     
               }
               return r;
           }
           
           
           
           
           
           
           
           
           
           
           
           
           public static double MDet3(double[][] A){
               
               double[][] Menor0 = new double[2][2];
               double[][] Menor1 = new double[2][2];
               double[][] Menor2 = new double[2][2];
               
               Menor0[0][0] = A[1][1];
               Menor0[0][1] = A[1][2];
               Menor0[1][0] = A[2][1];
               Menor0[1][1] = A[2][2];
               /*
               System.out.println("\n");
               System.out.println("Menor 0: ");
               Mshow(Menor0);
               System.out.println("\n");*/
               
               Menor1[0][0] = A[1][0];
               Menor1[0][1] = A[1][2];
               Menor1[1][0] = A[2][0];
               Menor1[1][1] = A[2][2];
               /*
               System.out.println("Menor 1: ");
               Mshow(Menor1);
               System.out.println("\n"); */
               
               Menor2[0][0] = A[1][0];
               Menor2[0][1] = A[1][1];
               Menor2[1][0] = A[2][0];
               Menor2[1][1] = A[2][1];
               /*
               System.out.println("Menor 2: ");
               Mshow(Menor2);
               System.out.println("\n"); */
               
               //System.out.println("A[0][0] * MDet2(Menor0) + A[0][1] * MDet2(Menor1) + A[0][2] * MDet2(Menor2)");
               //System.out.println("\n");
              // System.out.println(A[0][0] + "*" + MDet2(Menor0) + "+" + A[0][1] + "*" + MDet2(Menor1) + "+" + A[0][2] + "*" + MDet2(Menor2));
               //System.out.println("\n");
               double Det = A[0][0] * MDet2(Menor0) - A[0][1] * MDet2(Menor1) + A[0][2] * MDet2(Menor2);
              // System.out.println("\n");
               
               return Det;
           }
           
           public static double[][] Transpose(double[][] A){
            
            byte n = (byte) A.length;
            
            double[][]At = new double[n][n];
            
            for (byte i = 0; i < n; i++){
                
                for(byte j = 0 ; j < n; j++){
                
                    At[i][j] = A[j][i];
                    
                }
                
            }
            
            return At;
            
            }
           public static double[][] MInverse3(double[][] A){
            
               double Det = MDet3(A);
               double Detinv = 1.0/Det;
               
               double a = A[0][0];
               double b = A[0][1];
               double c = A[0][2];
               double d = A[1][0];
               double e = A[1][1];
               double f = A[1][2];
               double g = A[2][0];
               double h = A[2][1];
               double i = A[2][2];
               
               double[][] Adj = { {e*i - f*h,-(d*i - f*g), d*h-e*g},
                               {-(b*i - c*h), a*i - c*g,  -(a*h - b*g)},
                                 {b*f - c*e, -(a*f - c*d), a*e - b*d} };
           
           double[][] Inv = Transpose(MMultScalar(Adj, Detinv));
           
           return Inv;
        }
       
       
       
       public static void main(String[] args){
           
           double A[][] = {{1,2,2},{3,4,1},{1,2,0}};
           
           Mshow(A);
           System.out.println("\n Det: " + MDet3(A));
           
           Mshow(MInverse3(A));
           
           Mshow(MInverse3(MInverse3(A)));
           
           //Mshow(MMultScalar(A,2));
           
        }


}
