public class RemoveElement{

    public int removeElement(int[] nums, int val) {
        int k=0;
        int i= 0;
        while (i<nums.length && k<nums.length) {
            if(nums[i]!=val){
                nums[k]=nums[i];
                k++;
            }
            i++;
        }
        return k;
    }

    public static void main(String[] args) {
        RemoveElement solution= new RemoveElement();
        System.out.println(solution.removeElement(new int[]{3,2,2,3}, 3));
        System.out.println(solution.removeElement(new int[]{0,1,2,2,3,0,4,2}, 2));
    }
}