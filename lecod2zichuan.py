class Solution(object):
    def longestPalindrome(self, s):
      if len(s) == 0 or len(s) == 1:
         return s
      i=1
      new_string = ''
      arra =[]
      def ifwzc(testarr):
         kk=True
         j=0
         for num in range(0,int(len(testarr)/2)):
            if(testarr[num]==testarr[len(testarr)-1+j]):
               kk=True
            else:
               kk=False
               break
            j-=1
         return kk
      for index1 in s:
         str2=index1
         new_string = s[i:]
         for  index2 in  new_string:
            str2+=index2
            if(ifwzc(str2)):
               arra.append(str2)
         i+=1
      if len(arra) == 0:
         return s[0]
      return max(arra, key=len)
print(Solution.longestPalindrome(0,"accabcaa"))
 