class Solution: 
 def isPalindrome(x): 
        if (x < 0 or (x % 10 == 0 and x != 0)): 
         return 0;
        revertedNumber = 0
        while (x > revertedNumber): 
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        return x == revertedNumber or x == revertedNumber //10;
    

print(Solution.isPalindrome(123321))
