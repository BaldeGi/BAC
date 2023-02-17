import java.util.Arrays;

public class Matrix {

    public static void main(String[] args) {;
        String s ="1 2 3\n0 1 1";
        System.out.println(Arrays.deepToString(buildFrom(s)));
        System.out.println(sum(buildFrom(s)));
        System.out.println(Arrays.deepToString(transpose(buildFrom(s))));
        System.out.println(Arrays.deepToString(product(buildFrom(s),transpose(buildFrom(s)))));
    }

    /**
     * Create a matrix from a String.
     *
     * The string if formatted as follow:
     *  - Each row of the matrix is separated by a newline
     *    character \n
     *  - Each element of the rows are separated by a space
     *
     *  @param s The input String
     *  @return The matrix represented by the String
     */
    public static int [][] buildFrom(String s) {
        String [] a =s.split("\n");
        int [][] matrix = new int [a.length][];
        for (int i = 0; i < a.length; i++) {
            String [] b =a[i].split(" ");
            int [] l = new int [b.length];
            for(int j = 0;j<b.length;j++){
                l[j] = Integer.parseInt(b[j]);
            }
            matrix[i] = l;
        }
        return matrix;
    }

    /**
     * Compute the sum of the element in a matrix
     *
     * @param matrix The input matrix
     * @return The sum of the element in matrix
     */
    public static int sum(int[][] matrix) {
        int somme = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                somme+=matrix[i][j];
            }
        }
        return somme;
    }

    /**
     * Compute the transpose of a matrix
     *
     * @param matrix The input matrix
     * @return A new matrix that is the transpose of matrix
     */
    public static int[][] transpose(int[][] matrix) {
        int [][] mat = new int [matrix[0].length][matrix.length];
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j<mat[i].length; j++) {
                mat[i][j] = matrix[j][i];
            }
        }
        return mat;
    }

    /**
     * Compute the product of two matrix
     *
     * @param matrix1 A n x m matrix
     * @param matrix2 A m x k matrix
     * @return The n x k matrix product of matrix1 and matrix2
     */
    public static int[][] product(int[][] matrix1, int[][] matrix2) {
        int[][] mult = new int[matrix1.length][matrix2[0].length];
        if (matrix1[0].length == matrix2.length) {
            for (int i = 0; i < matrix1.length; i++) {
                for (int j = 0; j < matrix2[0].length; j++) {
                    for (int k = 0; k < matrix1[0].length; k++) {
                        mult[i][j] += (matrix1[i][k]) * (matrix2[k][j]);
                    }
                }
            }
            return mult;
        } return mult;
    }
}
