var solution= new Solution();

Console.WriteLine(solution.SumFourDivisors([21,4,7]));
Console.WriteLine(solution.SumFourDivisors([21,21]));
Console.WriteLine(solution.SumFourDivisors([1,2,3,4,5]));

public class Solution {
    public int SumFourDivisors(int[] nums) {
        int sum = 0;
        for (int i= 0 ; i<nums.Length; i++)
        {
            sum+=SumDivisors(nums[i]);
        }
        return sum;
    }

    private int SumDivisors(int num)
    {
        int sum = 0;
        int counter=0;
        int limit= (int)Math.Sqrt(num);
        for (int i = 1; i <= limit ; i++)
        {
            if(num%i == 0)
            {
                int other=  num/i;
                sum+= i;
                counter++;
                if (other != i)
                {
                    sum += other;
                    counter++;
                }
            }
        }
        return counter==4? sum:0;
    }
}