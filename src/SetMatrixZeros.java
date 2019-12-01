public class SetMatrixZeros {
    public void setZeroes(int[][] matrix) {
        int zero=-1111;
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if(matrix[i][j]==0){
                    for(int z=0;z<matrix.length;z++){
                        if(matrix[z][j]!=0)
                            matrix[z][j]=zero;
                    }
                    for(int z=0;z<matrix[0].length;z++){
                        if(matrix[i][z]!=0)
                            matrix[i][z]=zero;
                    }
                }
            }
        }
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if(matrix[i][j]==zero)
                    matrix[i][j]=0;
            }
        }
    }
}
