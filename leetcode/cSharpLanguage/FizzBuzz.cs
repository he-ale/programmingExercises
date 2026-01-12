using System;
using System.Collections.Generic;

var solution = new Solution();
Console.WriteLine(solution.FizzBuzz(3));
Console.WriteLine(solution.FizzBuzz(5));
Console.WriteLine(solution.FizzBuzz(15));

public class Solution {
    public IList<string> FizzBuzz(int n) {
        var nums= new List<string>();   
        for (int i = 1; i <= n; i++)
        {
            if (i % 15 == 0)
            {
                nums.Add("FizzBuzz");
            }
            else if (i % 3 == 0)
            {
                nums.Add("Fizz");
            }
            else if (i % 5 == 0)
            {
                nums.Add("Buzz");
            }
            else
            {
                nums.Add(i.ToString());
            }
        }     
        return nums;
    }
}