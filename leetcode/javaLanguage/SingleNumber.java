import java.util.HashMap;

public class SingleNumber {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> register= new HashMap<>();
        for(int num: nums){
            if(register.containsKey(num)){
                register.put(num, register.get(num)+1);
            }else{
                register.put(num, 1);
            }
        }
        for (int key : register.keySet()) {
            if(register.get(key)==1){
                return key;
            }
        }
        return 0;
    }
}
