class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
    
        if n==0:
            return 1
        
        xnb2 = self.myPow(x, abs(n)//2)
        xn = xnb2  * xnb2

        if abs(n) % 2 == 1:  
            xn = x * xn

        if  n < 1:
            xn = 1/xn
            
        return xn
        