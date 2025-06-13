class Solution:
    def reverse(x): 
        res = 0
        while(x!=0): 
            tmp = x%10
            print(tmp)
            if (res>214748364) or (res==214748364 and tmp>7):
                print('A')
                return 0
            if (res<-214748364) or (res==-214748364 and tmp<-8):
                print('B')
                return 0
            res = res*10 + tmp
            x //= 10
            print(x)
        return res    
print(Solution.reverse(9876))