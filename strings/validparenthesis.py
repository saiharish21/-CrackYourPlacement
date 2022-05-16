class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if s[0]==')' or  s[0]=='}' or  s[0]==']':
            return False
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            elif i==")":
                if len(stack)==0 or stack.pop()!="(":
                    return False
            elif i=="]":
                if len(stack)==0 or stack.pop()!="[":
                    return False
            elif i=="}":
                if len(stack)==0 or stack.pop()!="{":
                    return False
        return len(stack)==0
