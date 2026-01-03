public class ReverseInteger {
    public int reverse(int x) {
        int signal= x<0? -1:1;
        int num= Math.abs(x);
        int numReverse= 0;
        while (num!=0){
            int digit= num%10;
            if(numReverse>Integer.MAX_VALUE+digit)  return 0;
            numReverse= numReverse*10 +digit; 
            num/=10;
        }
        return numReverse*signal;
    }

    public static void main(String[] args) {
        ReverseInteger reverseInteger= new ReverseInteger();
        // System.out.println(reverseInteger.reverse(123));
        System.out.println(reverseInteger.reverse(1534236469));
        // System.out.println(reverseInteger.reverse(120));
    }
}
