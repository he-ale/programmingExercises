import java.util.HashSet;
import java.util.Set;

public class HappyNumber {
    public boolean isHappy(int n) {
        Set<Integer> nums= new HashSet<>();
        int num= 0;
        while (num!=1) {
            int sumDigits= 0;
            while (n>0) {
                int aux= n%10;
                sumDigits+=(aux*aux);
                n/=10;
            }
            if (sumDigits==1){
                num=sumDigits;
            }else{
                if(nums.contains(sumDigits)){
                    return false;
                }
                nums.add(sumDigits);
                n=sumDigits;
            }
        }
        return num==1;
    }

    public static void main(String[] args) {
        HappyNumber happyNumber= new HappyNumber();

        System.out.println(happyNumber.isHappy(19));
        System.out.println(happyNumber.isHappy(2));
        System.out.println(happyNumber.isHappy(3));
    }

}
