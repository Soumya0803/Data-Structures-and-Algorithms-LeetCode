class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        flag=True
        ipv4=queryIP.split('.')
        if len(ipv4)==4:
            for i in ipv4:
                if i=='' or (i[0] == '0' and len(i)!=1) or not i.isdigit() or int(i)>255:
                    flag=False
                    break
            if  flag:
                return 'IPv4'
        flag=True
        ipv6=queryIP.split(':')
        if len(ipv6)==8:
            for i in ipv6:
                if i=='' or len(i)>4 or not all(c in hexdigits for c in i):
                    flag=False
                    break
            if flag:
                return 'IPv6'
        return 'Neither'
                    
                
        
        
        
     
        