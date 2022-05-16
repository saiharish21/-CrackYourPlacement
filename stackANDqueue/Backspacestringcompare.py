class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1,l2=[],[]
        for i in range(0,len(s)):
            if s[i]!='#':
                l1.append(s[i])
            elif l1:
                l1.pop()
        for i in range(0,len(t)):
            if t[i]!='#':
                l2.append(t[i])
            elif l2:
                l2.pop()
        c1=''.join(l1)
        c2="".join(l2)
        if c1==c2:
            return True
        return False
