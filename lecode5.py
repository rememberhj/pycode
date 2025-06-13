class Solution(object):
    def myAtoi(self, s):
        i, j, l = 0, 0, len(s)
        ans = 0
        signed = 1
        upper_bound, lower_bound = 2 ** 31 - 1, -2 ** 31
        while i < l and s[i] == " ":
            print(s[i]== " ")
            i += 1
            
            print('1')
        if i < l and (s[i] == "+" or s[i] == "-"):
            signed = -1 if s[i] == "-" else 1
            i += 1
            print('2')
        while i < l and s[i] == "0":
            i += 1
            print('3')
        while i < l and s[i].isdigit():
            print('4')
            ans = ans * 10 + int(s[i]) * signed
            print(ans)
            print(signed)
            if signed > 0 and ans > upper_bound:
                return upper_bound
            if signed < 0 and ans < lower_bound:
                return lower_bound
            i += 1
        return ans
    

#print(Solution.myAtoi('AA','9-8764566'))
print(Solution.myAtoi('AA','999888'))
350001518531