import java.util.HashMap;

public class RomanToInteger {
    private HashMap<Character, Integer> values;

    public RomanToInteger(){
        values= new HashMap<>();
        values.put('I', 1);
        values.put('V', 5);
        values.put('X', 10);
        values.put('L', 50);
        values.put('C', 100);
        values.put('D', 500);
        values.put('M', 1000);
    }

    public int romanToInt(String s) {
        int result= 0;
        char prev=s.charAt(s.length()-1);
        for (int i= s.length()-1; i>=0; i--) {
            if(result==0){
                result+=values.get(s.charAt(i));
            }else if (result>values.get(s.charAt(i)) && prev!=s.charAt(i)){
                result= result-values.get(s.charAt(i));
            }else{
                result= result+values.get(s.charAt(i));
            }
            prev= s.charAt(i);
        }
        return result;
    }

    public static void main(String[] args) {
        var solution= new RomanToInteger();
        System.out.println(solution.romanToInt("III"));
        System.out.println(solution.romanToInt("LVIII"));
        System.out.println(solution.romanToInt("MCMXCIV"));
    }
}
