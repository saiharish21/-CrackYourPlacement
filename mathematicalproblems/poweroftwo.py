class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      return n!=0 and (n & n-1)==0        
# Any power of 2 minus 1 is all ones: (2 N - 1 = 111....b)

# 2 = 2^1.  2-1 = 1 (1b)
# 4 = 2^2.  4-1 = 3 (11b)
# 8 = 2^3.  8-1 = 7 (111b)
# Take 8 for example. 1000 & 0111 = 0000

# So that expression tests if a number is NOT a power of 2.
        
        
        
        
#         for i in range(0,1000):
#             if 2**i==n:
#                 return True
#         return False
          
    
    
      #1087 / 1108 test cases passed.
      # while n!=1:
      #   if n%2!=0:
      #       return False
      #   n=n//2
      # return True
