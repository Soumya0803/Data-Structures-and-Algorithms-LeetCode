class Solution(object):
    def reverseOnlyLetters(self, S):
        ans=[]
        index=len(ans)-1
        
        for i,x in enumerate(S):
            if x.isalpha():
                while not S[index].isalpha():
                    index-=1
                ans.append(S[index])
                index-=1
                
            else:
                ans.append(x)
        return "".join(ans)