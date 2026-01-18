public class ClimbingStairs {

    public int climbStairs(int n) {
        if( n==1 ){
            return 1;
        }    
        if( n==2 ){
            return 2;
        }
        int a= 1;
        int b= 2;
        int current= 0;
        int i=3;
        while (i<=n) {
            current= a+b;
            a=b;
            b=current;
            i++;
        }
        return current;
    }

    public static void main(String[] args) {
        ClimbingStairs solution= new ClimbingStairs();

        System.out.println(solution.climbStairs(2));
        System.out.println(solution.climbStairs(3));
        System.out.println(solution.climbStairs(4));
        System.out.println(solution.climbStairs(5));
        System.out.println(solution.climbStairs(8));
    }
}