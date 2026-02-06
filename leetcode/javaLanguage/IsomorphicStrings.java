import java.util.HashMap;

public class IsomorphicStrings {

    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> mapS=new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if(mapS.containsKey(s.charAt(i))){
                if(mapS.get(s.charAt(i))!=t.charAt(i)){
                    return false;
                }
            }else if(mapS.containsValue(t.charAt(i))){
                return false;
            }
            else{
                mapS.put(s.charAt(i), t.charAt(i));
            }
        }
        return true;
    }

    public static void main(String[] args) {
        IsomorphicStrings solution= new IsomorphicStrings();

        System.out.println(solution.isIsomorphic("egg", "add"));
        System.out.println(solution.isIsomorphic("f11", "b23"));
        System.out.println(solution.isIsomorphic("paper", "title"));
        System.out.println(solution.isIsomorphic("badc", "baba"));
    }
}