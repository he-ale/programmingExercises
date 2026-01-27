public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        String prefix= strs[0];

        for(int i= 1; i<strs.length; i++){
            prefix= findPrefix(prefix, strs[i]);
        }
        return prefix;
    }

    private String findPrefix(String str1, String str2){
        String aux1, aux2;
        if(str1.length()>str2.length()){
            aux1= str2;
            aux2= str1;
        } else {
            aux1= str1;
            aux2= str2;    
        }
        StringBuilder prefix= new StringBuilder();
        for(int i= 0; i<aux1.length(); i++){
            if(aux1.charAt(i)==aux2.charAt(i)){
                prefix.append(aux1.charAt(i));
            }else{
                return prefix.toString();
            }
        }
        return prefix.toString();
    }

    public static void main(String[] args) {
        LongestCommonPrefix solution= new LongestCommonPrefix();
        System.out.println(solution.longestCommonPrefix(new String[]{"flower","flow","flight"}));
        System.out.println(solution.longestCommonPrefix(new String[]{"dog","racecar","car"}));
    }
}
