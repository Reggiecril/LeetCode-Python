public class TwoSumIIInputarrayissorted {
    public int[] twoSum(int[] numbers, int target) {
        int[] sum=new int[2];
        for (int i = numbers.length-1; i >=0 ; i--) {
            int last=target-numbers[i];
            if (last<=0&&target>0)
                continue;
            int j=0;
            while (j<i){
                if (last==numbers[j]){
                    sum[0]=j+1;
                    sum[1]=i+1;
                    return sum;
                }else if(last<numbers[j]){
                    break;
                }
                j++;
            }
        }
        return sum;
    }
}
