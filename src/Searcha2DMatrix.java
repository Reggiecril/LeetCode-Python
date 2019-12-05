public class Searcha2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix==null||matrix.length==0||matrix[0].length==0)
            return false;
        if (target<matrix[0][0]||target>matrix[matrix.length-1][matrix[0].length-1])
            return false;
        for (int i = 0; i < matrix.length; i++) {
            if (i==matrix.length-1)
                return searchArray(matrix[i],target);
            if (target>=matrix[i][0]&&target<matrix[i+1][0])
                return searchArray(matrix[i],target);
            else continue;
        }
        return false;
    }
    private boolean searchArray(int[] num,int target){
        int left=0,right=num.length-1;
        while (left<=right){
            int mid=left+(right-left)/2;
            if (num[mid]>target){
                right=mid-1;
            }else if (num[mid]<target){
                left=mid+1;
            }else return true;
        }
        return false;
    }
}
